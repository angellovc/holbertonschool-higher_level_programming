#!/usr/bin/python3
""" sends a request to the URL and
displays the body of the response
or status error
"""
from urllib import request
from sys import argv
import urllib


if __name__ == "__main__":
    url = argv[1]
    req = request.Request(url)
    try:
        with request.urlopen(url) as response:
            print(response.read().decode())
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))
