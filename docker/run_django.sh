docker run -d -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock \
	-v /Users/dmishin/code/seedme2demo/stats:/var/stats \
	-e "VIRTUAL_HOST=demo.seedme.org" \
	-e "VIRTUAL_PORT=8000" \
	docker-demo

#-e "LETSENCRYPT_HOST=demo.seedme.org" \
#-e "LETSENCRYPT_EMAIL=amit@sdsc.edu" \
