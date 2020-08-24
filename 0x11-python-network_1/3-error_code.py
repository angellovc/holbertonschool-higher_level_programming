#!/bin/usr/python3
""" sends a request to the URL and
displays the body of the response
or status error
"""
from urllib import request
from urllib import parse
from sys import argv
import urllib


if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    try:
        response = request.urlopen(url)
        print(response.read().decode())
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
