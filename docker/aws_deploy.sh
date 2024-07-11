#!/bin/bash

if [ -z "$AWS_IP_ADDRESS" ]
then
  echo "AWS_IP_ADDRESS not defined"
  exit 0
fi

git archive --format tar --output ./project.tar main

echo 'Uploading project ..... :-) .... Be Patient!'
rsync -e "ssh -i authors_key.pem" ./project.tar towhid@$AWS_IP_ADDRESS:/tmp/project.tar
echo 'Upload complete... :-)'

echo 'Building the image...'
ssh -i "authors_key.pem" -o StrictHostKeyChecking=no towhid@$AWS_IP_ADDRESS << 'ENDSSH'
    sudo mkdir -p /app
    sudo rm -rf /app/* && sudo tar -xf /tmp/project.tar -C /app
    sudo docker compose -f /app/production.yml up --build -d --remove-orphans
ENDSSH

echo 'Build completed Successfully... :-)'
