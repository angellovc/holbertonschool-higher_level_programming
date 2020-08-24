#!/usr/bin/python3
""" request module """
from urllib import request
from urllib import parse

data = {}
url = "https://intranet.hbtn.io/status"

with request.urlopen(url) as response:
    http = response.read()
    print("Body response:")
    print("	- type: {}".format(type(http)))
    print("	- content: {}".format(http))
    print("	- utf8 content: {}".format(http.decode()))
