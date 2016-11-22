from django.shortcuts import render

from docker import Client

import socket

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

    if(request.GET.get('action',None)):
        if(request.GET['action'] == "start" and not container_id):
            port = pick_unused_port();
            container = cli.create_container(
                image='seedme2', ports=[80],
                host_config=cli.create_host_config(port_bindings={
                    80: port,
                })
            )
            container_id = container['Id'][:7]
            request.session['container_id'] = container_id
            request.session['port'] = port
            cli.start(container_id)

        if(request.GET['action'] == "stop" and container_id):
            cli.remove_container(
                container=container_id,
                force = True
            )
            container_id = None
            del request.session['container_id']
            del request.session['port']

    port = request.session.get('port') or ""

    return render(request, 'templates/index.html', {
        'running_container': container_id,
        'port': port
    }, content_type='application/xhtml+xml')