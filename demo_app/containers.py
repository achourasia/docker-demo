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

        # TODO: Generate the credentials for the mysql db dynamically and use some more secure credentials!

        # self.mysql_db_container_name = "%s_mysql_db" % self.name
        # self.mysql_db_volume_name = "%s_mysql_data_volume" % self.name
        # self.mysql_auth = {
        #     "MYSQL_ROOT_PASSWORD": "mysql_root_password",
        #     "MYSQL_USER": "mysql_drupal",
        #     "MYSQL_PASSWORD": "mysql_drupal_some_password",
        #     "MYSQL_DATABASE": "drupal"
        # }
        #
        # # First, start a new mysql db container just for this demo container
        # self.mysql_db_container = cli.containers.run(
        #     detach=True,
        #     name=self.mysql_db_container_name,
        #     image=settings.DOCKER['MYSQL_DB_IMAGE'],
        #     entrypoint=['/entrypoint.sh', '--default-authentication-plugin=mysql_native_password'],
        #     environment=self.mysql_auth,
        #     restart_policy={"Name": "always"},
        #     volumes={
        #         self.mysql_db_volume_name: {
        #             'bind': '/var/lib/mysql',
        #             'mode': 'rw'
        #         }
        #     },
        #     network=self.network
        # )
        #
        # # Bundle the mysql credentials needed to pass to the drupal container
        # self.mysql_db_uri_config = self.mysql_auth
        # self.mysql_db_uri_config['MYSQL_HOST'] = self.mysql_db_container_name
        # self.mysql_db_uri = 'mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}/{MYSQL_DATABASE}'.format(
        #     **self.mysql_db_uri_config)

        self.seedme2_demo_container = cli.containers.run(
            detach=True,
            image=self.image, ports={'80/tcp': self.port},
            name=self.name,
            environment={"VIRTUAL_HOST": "%s.%s" % (self.name, request_host)},  # "MYSQL_DB_URI": self.mysql_db_uri},
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
        # First, destroy the mysql container & its volume
        # mysql_db_container_name = "%s_mysql_db" % seedme2_demo_container_name
        # try:
        #     cli.containers.get(mysql_db_container_name).remove(
        #         force=True,
        #         v=True  # Remove the attached volumes
        #     )
        # except:
        #     pass

        # Then, destroy the drupal container
        try:
            cli.containers.get(seedme2_demo_container_name).remove(
                force=True,
                v=True  # Remove the attached volumes
            )
        except:
            pass
