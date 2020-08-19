#!/bin/bash
#chatch it
curl -si -X "PUT" -d "user_id=98" -H "origin: HolbertonSchool" -L 0.0.0.0:5000/catch_me
