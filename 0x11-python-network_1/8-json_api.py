#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter
"""
import requests
import json
from sys import argv

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if argv[1]:
        data = {'q': argv[1]}
    else:
        data = {'q': ''}
    response = requests.post(url, data=data)
    try:
        body = json.loads(response.text)
        id = body.get('id')
        name = body.get('name')
        if id is None:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except:
        print("Not a valid JSON")
