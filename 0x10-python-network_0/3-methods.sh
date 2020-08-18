#!/bin/bash
#show the http response opstions
curl -sI "$1" | grep Allow | tr -d 'Allow: '
