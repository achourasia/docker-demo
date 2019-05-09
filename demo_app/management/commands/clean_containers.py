import time

from django.contrib.sessions.models import Session
from django.core.management.base import BaseCommand
from docker import DockerClient

from demo_app.containers import Seedme2DemoContainer


class Command(BaseCommand):
    help = 'Cleans the expired containers'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        cli = DockerClient(base_url='unix://var/run/docker.sock')
        sessions = Session.objects.all()
        for session in sessions:
            data = session.get_decoded()
            if (data.get("container_name", None) and data.get("container_exp") < time.time()):
                container_name = data["container_name"]

                # Destroy this provisioned seedme2 demo app container(s)
                Seedme2DemoContainer.destroy(seedme2_demo_container_name=container_name)

                session.delete()
                self.stdout.write(self.style.SUCCESS('Successfully cleaned container %s' % container_name))
