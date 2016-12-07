# docker-demo

## The project allows spawning docker containers of a certain type on request from a web page and destroying after a period of time

- Build docker-demo image with django app

```docker build -t docker-demo .```

- Build nginx proxy image

```pushd proxy && docker build -t nginx-proxy . && popd```

- Run the service containers

```
docker/run_proxy.sh
docker/run_django.sh
```
