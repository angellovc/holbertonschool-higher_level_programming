#!/usr/bin/python3
""" sends a request to the URL and displays the value
of the variable X-Request-Id in the response header
"""
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
