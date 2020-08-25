#!/usr/bin/python3
""" sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    response = requests.get(url)
    try:
        response.raise_for_status()
        print(response.text)
    except:
        print("Error code: {}".format(response.status_code))
