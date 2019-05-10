from django.conf import settings
from docker import DockerClient

from demo_app.utils import stats_utils
from demo_app.utils.docker_utils import pick_unused_port
from demo_app.utils.name_utils import get_random_name

cli = DockerClient(base_url=settings.DOCKER["DOCKER_SOCKET_PATH"])


class Seedme2DemoContainer:

    def __init__(self, request_host, network=settings.DOCKER["NETWORK"],
                 image=settings.DOCKER["SEEDME2_CONTAINER_IMAGE"], restart_policy="always", record_stats=True):
        self.image = image
        self.restart_policy = {"Name": restart_policy}
        self.network = network
        self.port = pick_unused_port()
        self.name = get_random_name("-")
        self.request_host = request_host

        self.seedme2_demo_container = cli.containers.run(
            detach=True,
            image=self.image, ports={'80/tcp': self.port},
            name=self.name,
            environment={"VIRTUAL_HOST": "%s.%s" % (self.name, request_host)},
            restart_policy=self.restart_policy,
            network=self.network
        )

        self.seedme2_user_password = self.seedme2_demo_container.exec_run("/init.sh", detach=False).output.decode(
            "utf-8").strip()

        # Record the stats for the container
        if record_stats:
            stats_utils.record_container_stats(container_name=self.name)

    @staticmethod
    def destroy(seedme2_demo_container_name):
        try:
            cli.containers.get(seedme2_demo_container_name).remove(
                force=True,
                v=True  # Remove the attached volumes
            )
        except:
            pass
