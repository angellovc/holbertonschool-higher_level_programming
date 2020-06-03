#!/usr/bin/python3
""" from json to python """
import json


def from_json_string(my_str):
    """ Get a python object from json string """
    return json.loads(my_str)
