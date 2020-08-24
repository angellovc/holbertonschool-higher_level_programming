#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """
import requests


if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    response = requests.get(url)
    print("Body response:$")
    print("	- type: {}".format(type(response)))
    print("	- content: {}".format(response.text))
