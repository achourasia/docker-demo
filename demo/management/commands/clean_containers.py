from django.core.management.base import BaseCommand, CommandError
from django.contrib.sessions.models import Session
from docker import Client

import time

class Command(BaseCommand):
    help = 'Cleans the expired containers'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        cli = Client(base_url='unix://var/run/docker.sock')
        sessions = Session.objects.all()
        for session in sessions:
            data = session.get_decoded()
            if(data.get("container_name", None) and data.get("container_exp") < time.time()):
                container_id = data["container_id"]
                try:
                    #cli.remove_container(
                    #    container=container_id,
                    #    force = True
                    #)
                    pass
                except:
                    pass
                #session.delete()
                self.stdout.write(self.style.SUCCESS('Successfully cleaned container %s'%container_id))
