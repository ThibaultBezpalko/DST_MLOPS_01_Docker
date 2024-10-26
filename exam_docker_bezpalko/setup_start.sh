#!/bin/bash

# Build the image of the container used for the authentication test
cd ~/DST_MLOPS/01_Docker/exam_docker_bezpalko/docker_image_authentication
docker image build . -t image_authentication:latest

# Build the image of the container used for the authentication test
cd ~/DST_MLOPS/01_Docker/exam_docker_bezpalko/docker_image_authorization
docker image build . -t image_authorization:latest

# Build the image of the container used for the content test
cd ~/DST_MLOPS/01_Docker/exam_docker_bezpalko/docker_image_content
docker image build . -t image_content:latest

# Create a volume that will be shared by the containers
docker volume create --name exam_docker_bezpalko_volume

# Move the python files to the volume shared by the containers
sudo cp ~/DST_MLOPS/01_Docker/exam_docker_bezpalko/docker_image_authentication/test_authentication.py /var/lib/docker/volumes/exam_docker_bezpalko_volume/_data/
sudo cp ~/DST_MLOPS/01_Docker/exam_docker_bezpalko/docker_image_authorization/test_authorization.py /var/lib/docker/volumes/exam_docker_bezpalko_volume/_data/
sudo cp ~/DST_MLOPS/01_Docker/exam_docker_bezpalko/docker_image_content/test_content.py /var/lib/docker/volumes/exam_docker_bezpalko_volume/_data/

# Start the containers
cd ~/DST_MLOPS/01_Docker/exam_docker_bezpalko
docker-compose up

