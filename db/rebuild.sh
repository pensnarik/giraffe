#!/usr/bin/env bash

docker-compose rm -f database
docker build . -t giraffe
docker-compose up