#!/usr/bin/python3
""" sends a POST request to the
passed URL with the email as a parameter
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    email = {'email': argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
