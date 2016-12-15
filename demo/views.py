from django.shortcuts import render

from django.views.decorators.csrf import csrf_exempt
from docker import DockerClient
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

    cli = DockerClient(base_url='unix://var/run/docker.sock')

    container_name = None
    password = None
    if request.session.get('container_name', None):
        container_name = request.session['container_name']
        password = request.session['password']

    if(request.POST.get('action',None)):
        if(request.POST['action'] == "start" and not container_name):
            port = pick_unused_port();
            container_name = namesgenerator.get_random_name()
            container = cli.containers.run(
                detach=True,
                image='seedme2', ports={'80/tcp':port},
                name=container_name,
                environment = {"VIRTUAL_HOST":"%s.%s"%(container_name, request.get_host())}
            )
            request.session['container_name'] = container_name
            request.session['container_exp'] = time.time()+settings.CONTAINER_EXPIRATION
            password = container.exec_run("/init.sh", detach=False)

            request.session['password'] = password

        if(request.POST['action'] == "stop" and container_name):
            try:
                cli.containers.get(container_name).remove(
                    force = True
                )
            except:
                pass
            del request.session['container_name']
            del request.session['container_exp']
            del request.session['password']
            container_name = None
            password = None

    return render(request, 'templates/index.html', {
        'running_container': container_name,
        'expiration': (request.session.get('container_exp') or 0)*1000,
        'password': "%s"%(password)
    }, content_type='application/xhtml+xml')
