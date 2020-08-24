#!/usr/bin/python3
""" Python script that takes in a URL
isplays the value of the X-Request-Id
variable found in the header of the response
"""
from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    data = {}
    url = argv[1]

    with request.urlopen(url) as response:
        print(response.getheader("X-Request-Id"))
