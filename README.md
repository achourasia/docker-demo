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

##Commiting a new seedme2 container
```
docker commit -m "<Commit message>" <container-name> seedme2:8.2.4.<new number>
docker tag seedme2:8.2.4.<number> seedme2:latest

```

For example:

```
docker commit -m "Last brushing up" prickly-hoover seedme2:8.2.4.5
docker tag seedme2:8.2.4.5 seedme2:latest
```
