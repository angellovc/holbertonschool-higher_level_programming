#!/usr/bin/python3
""" obj to json string module """
import json


def to_json_string(my_obj):
    """ convert some object into a json string """
    return json.dumps(my_obj)
