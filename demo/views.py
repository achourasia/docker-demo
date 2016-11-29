from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from docker import Client
from django.conf import settings
import socket
import time
import namesgenerator

from django.http import HttpResponse

def pick_unused_port():
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.bind(('localhost', 0))
  addr, port = s.getsockname()
  s.close()
  return port

def index(request):

    cli = Client(base_url='unix://var/run/docker.sock')

    container_id = None

    if request.session.get('container_id', None):
        container_id = request.session['container_id']

    if(request.POST.get('action',None)):
        if(request.POST['action'] == "start" and not container_id):
            port = pick_unused_port();
            container_name = namesgenerator.get_random_name()
            container = cli.create_container(
                image='seedme2', ports=[80],
                name=container_name,
                environment = {"VIRTUAL_HOST":"%s.%s"%(container_name, request.get_host)},
                host_config=cli.create_host_config(port_bindings={
                    80: port,
                })
            )
            container_id = container['Id'][:7]
            request.session['container_name'] = container_name
            request.session['container_exp'] = time.time()+settings.CONTAINER_EXPIRATION
            cli.start(container_id)

        if(request.POST['action'] == "stop" and container_id):
            try:
                cli.remove_container(
                    container=container_id,
                    force = True
                )
            except:
                pass
            del request.session['container_id']
            del request.session['container_exp']

    return render(request, 'templates/index.html', {
        'running_container': container_name,
        'expiration': (request.session.get('container_exp') or 0)*1000
    }, content_type='application/xhtml+xml')