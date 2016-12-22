#mkdir -p `dirname "$0"`/../certs

#docker run -d -p 80:80 -p 443:443 \
#    --name nginx-proxy \
#    -v /Users/dmishin/code/seedme2demo/certs:/etc/nginx/certs:ro \
#    -v /etc/nginx/vhost.d \
#    -v /usr/share/nginx/html \
#    -v /var/run/docker.sock:/tmp/docker.sock:ro \
#    nginx-proxy

#docker run -d \
#    -v /Users/dmishin/code/seedme2demo/certs:/etc/nginx/certs:rw \
#    --volumes-from nginx-proxy \
#    -v /var/run/docker.sock:/var/run/docker.sock:ro \
#    alastaircoote/docker-letsencrypt-nginx-proxy-companion
#    jrcs/letsencrypt-nginx-proxy-companion

docker run -d -p 80:80 -v /var/run/docker.sock:/tmp/docker.sock nginx-proxy
