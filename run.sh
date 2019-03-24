#!/bin/bash

docker build -t flaskimage .

docker run --name flaskcontainer -p 80:80 flaskimage

