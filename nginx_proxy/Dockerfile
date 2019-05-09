FROM jwilder/nginx-proxy:alpine
RUN { \
	echo 'client_max_body_size       512M;'; \
	echo 'client_body_buffer_size    128k;'; \
	echo 'proxy_connect_timeout      10m;'; \
	echo 'proxy_send_timeout         10m;'; \
	echo 'proxy_read_timeout         10m;'; \
	echo 'proxy_buffer_size          4k;'; \
	echo 'proxy_buffers              4 32k;'; \
	echo 'proxy_busy_buffers_size    64k;'; \
	echo 'proxy_temp_file_write_size 64k;'; \
    } > /etc/nginx/conf.d/drupal_proxy.conf