#!/bin/bash

if [ -z "$AWS_IP_ADDRESS" ]
then
    echo "AWS_IP_ADDRESS not defined"
    exit 1
fi

git archive --format tar --output ./project.tar main

echo 'Uploading project ..... :-) .... Be Patient!'
rsync -e "ssh -i /media/towhid/Projects/aws_keys/authors_key.pem" ./project.tar ubuntu@$AWS_IP_ADDRESS:~/project.tar
echo 'Upload complete... :-)'

# Transfer .django and .postgres files separately
echo 'Uploading environment files...'
rsync -e "ssh -i /media/towhid/Projects/aws_keys/authors_key.pem" ./.envs/.production/.django ubuntu@$AWS_IP_ADDRESS:~/django_env
rsync -e "ssh -i /media/towhid/Projects/aws_keys/authors_key.pem" ./.envs/.production/.postgres ubuntu@$AWS_IP_ADDRESS:~/postgres_env
echo 'Environment files uploaded... :-)'

echo 'Building the image...'
ssh -i "/media/towhid/Projects/aws_keys/authors_key.pem" -o StrictHostKeyChecking=no -t ubuntu@$AWS_IP_ADDRESS << 'ENDSSH'
sudo mkdir -p /app
sudo rm -rf /app/*
sudo tar -xf ~/project.tar -C /app

sudo mkdir -p /app/.envs/.production
sudo mv ~/django_env /app/.envs/.production/.django
sudo mv ~/postgres_env /app/.envs/.production/.postgres

# Check if .django file exists
if [ ! -f /app/.envs/.production/.django ]; then
    echo "Error: .django file is missing. Please ensure it exists in your project repository."
    exit 1
fi

# Check if .postgres file exists
if [ ! -f /app/.envs/.production/.postgres ]; then
    echo "Error: .postgres file is missing. Please ensure it exists in your project repository."
    exit 1
fi

# Run docker compose
sudo docker compose -f /app/production.yml up --build -d --remove-orphans
ENDSSH

if [ $? -eq 0 ]; then
    echo 'Build completed Successfully... :-)'
else
    echo 'Build failed. Please check the error messages above.'
fi