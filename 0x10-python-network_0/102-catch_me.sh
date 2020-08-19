#!/bin/bash
#chatch it
curl -si -X "PUT" -d "user_id=98" -H "origin: HolbertonSchool" -L "$1"
