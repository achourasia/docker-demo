docker run -d -p 8000:8000 -v /var/run/docker.sock:/var/run/docker.sock -e "VIRTUAL_HOST=seedmini4.sdsc.edu" -e "VIRTUAL_PORT=8000" docker-demo
