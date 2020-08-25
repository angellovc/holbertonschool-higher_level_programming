#!/usr/bin/python3
""" sends a POST request to http://0.0.0.0:5000/search_user
with the letter as a parameter """
import requests
from sys import argv


def load_json(json):
    data = {}
    if json.find("{") is -1 and json.find("}") is -1:
        raise TypeError('Not a valid JSON')
    if len(json) < 4:
        raise ValueError('No result')
    json = json.replace("{", "")
    json = json.replace("}", "")
    json = json.replace('\n', "")
    json = json.replace("\"", "")
    json = json.split(",")
    for item in json:
        item = item.split(':')
        if item[0] == 'id':
            data[item[0]] = int(item[1])
        else:
            data[item[0]] = item[1]
    return data

if __name__ == "__main__":
    if len(argv) > 1 and argv[1]:
        data = {'q': argv[1]}
    else:
        data = {'q': ''}
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data)
    try:
        values = load_json(response.text)
        id = values.get('id')
        name = values.get('name')
        print("[{}] {}".format(id, name))
    except TypeError as Error:
        print(Error)
    except ValueError as Error:
        print(Error)
