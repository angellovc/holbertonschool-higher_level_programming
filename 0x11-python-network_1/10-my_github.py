#!/usr/bin/python3
""" takes your Github credentials (username and password)
and uses the Github API to display your id """
import requests
import sys
token = sys.argv[2]
user = sys.argv[1]
response = requests.get('https://api.github.com/user', auth=(user, token))
print(response.json().get('id'))
