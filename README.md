# ms-rec

## Pre-requis:
- docker
- siege

## Technology:
Framework: Falcon
Datastore: Redis
Webserver: gunicorn

PoC for intersection of data using Redis

## Installation: 
run docker-compose up
This command will start the webserver

## Generate the data
This use a sample test of data. Increase if you want
1. Go into the docker container using the command "docker exec -it [CONTAINER ID] bash
2. run python generator.py

## Run load test
Out side of the container
- run siege -b -t10s -c10  -b -f tests/load/urls.txt 
