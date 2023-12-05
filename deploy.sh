#!/bin/bash

# Build the Docker image
docker build -t latex-ocr .

# Authenticate Docker to your Amazon ECR registry
aws ecr get-login-password --region region | docker login --username AWS --password-stdin your-ecr-repo-url

# Tag your image to match your repository
docker tag latex-ocr:latest your-ecr-repo-url/latex-ocr:latest

# Push this image to your newly created AWS repository
docker push your-ecr-repo-url/latex-ocr:latest