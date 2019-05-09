import time

from django.conf import settings
from django.shortcuts import render

from demo_app.containers import Seedme2DemoContainer


def home(request):
    container_name = None
    password = None

    if request.session.get('container_name', None):
        container_name = request.session['container_name']
        password = request.session['password']

    if (request.POST.get('action', None)):
        if (request.POST['action'] == "start" and not container_name):
            # Create a new docker container based on the seedme2 image
            seedme2_demo_container = Seedme2DemoContainer(request_host=request.get_host(), record_stats=True)
            container_name = seedme2_demo_container.name

            # Register the container information in the request's session
            request.session['container_name'] = container_name
            request.session['container_exp'] = time.time() + settings.DOCKER['CONTAINER_EXPIRATION']

            password = seedme2_demo_container.seedme2_user_password
            request.session['password'] = password

        if (request.POST['action'] == "stop" and container_name):
            # Destroy the SeedMe demo app.
            Seedme2DemoContainer.destroy(seedme2_demo_container_name=container_name)

            # Clear the request's session data containing info about this container that we're deleting
            del request.session['container_name']
            del request.session['container_exp']
            del request.session['password']

            container_name = None
            password = None

    return render(request, "home.html", {
        'running_container': container_name,
        'expiration': (request.session.get('container_exp') or 0) * 1000,
        'password': "%s" % (password)
    })
