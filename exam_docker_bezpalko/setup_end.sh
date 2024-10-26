#!/bin/bash

# Retrieve the log file
sudo cp /var/lib/docker/volumes/exam_docker_bezpalko_volume/_data/api_test.log ~/DST_MLOPS/01_Docker/exam_docker_bezpalko

# Stop and remove the containers 
docker-compose down --remove-orphans

# Delete the images
docker image rm image_authentication:latest
docker image rm image_authorization:latest
docker image rm image_content:latest

# (optional) Delete the log file in the volume
# sudo rm -fr /var/lib/docker/volumes/exam_docker_bezpalko_volume/_data/api_test.log

# Delete the volume 
docker volume rm exam_docker_bezpalko_volume