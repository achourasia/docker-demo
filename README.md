# Seedme Sandbox website
A Django-based demo website for trying & testing the Seedme application.

## Setup
#### 1. Create a separate Docker network for the sandbox website, called **seedme**
`docker network create seedme`

#### 2. Build the nginx-proxy & django app images
`docker-compose build`

#### 3. Run the app
Before running this step, make sure you already have a docker image called `seedme2`, which this sandbox application will use to spawn new seedme demo containers.

`docker-compose up -d`

Once the app is running, go to <a href="try.seedme.org" target="_blank">try.seedme.org</a> (and make sure that <a href="try.seedme.org" target="_blank">try.seedme.org</a> is added to your /etc/hosts file).

#### 4. Stop the app
`docker-compose down`

If you'd also like to remove the volumes associated with the containers, run `docker-compose down -v`.


## File structure
This app follows a conventional Django project file structure
-  `nginx_proxy/` holds the Dockerfile to build the nginx-proxy
- `demo_app/` is the folder for the "seedme2 demo" django app
- `stats/` is the folder containing the stats files for the "seedme2 demo" django app
- `drupal/` contains a Dockerfile for building a sample `seedme` Docker image (which was copied over from the initial project)
- `webapp/` is the folder for the `seedme2_webapp` django project

## Settings
In the `seedme2_webapp/settings.py` file, you can edit the following settings in the `DOCKER` dictionary to configure the app to fit your needs:
- `CONTAINER_EXPIRATION` (default: 7 days) - The number of seconds that a newly-spawned demo container can live for
- `SEEDME2_CONTAINER_IMAGE` (default: `"seedme2"`) - The Docker image name that holds the seedme application
- `DOCKER_SOCKET_PATH` (default: `"unix://var/run/docker.sock"`) - The host path to the docker.sock file.
- `NETWORK` (default: `"seedme"`) - The Docker network to use to deploy this sandbox application (and all of its associated containers)
    - Note that if you change this setting, you also have to edit the network name provided in the `docker-compose.yml` file.