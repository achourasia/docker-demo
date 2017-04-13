from django.core.management.base import BaseCommand, CommandError
from django.contrib.sessions.models import Session
from docker import DockerClient

import time

class Command(BaseCommand):
    help = 'Cleans the expired containers'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        cli = DockerClient(base_url='unix://var/run/docker.sock')
        sessions = Session.objects.all()
        for session in sessions:
            data = session.get_decoded()
            if(data.get("container_name", None) and data.get("container_exp") < time.time()):
                container_name = data["container_name"]
                try:
                    cli.containers.get(container_name).remove(force=True)
                except:
                    pass
                session.delete()
                self.stdout.write(self.style.SUCCESS('Successfully cleaned container %s'%container_name))
