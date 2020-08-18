#!/bin/bash
#show the http response opstions
curl -sI "$1" | grep Allow | awk '{print substr($0, index($0,$2))}'
