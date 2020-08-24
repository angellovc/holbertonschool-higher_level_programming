#!/usr/bin/python3
"""  sends a POST request to the passed
URL with the email as a parameter
"""
from urllib import request
from urllib import parse
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    data = parse.urlencode(email)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        print(response.read().decode())
