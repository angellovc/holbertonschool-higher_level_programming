#!/usr/bin/python3
""" load from json file module """
import json


def load_from_json_file(filename):
    """ load a python obj from json file """
    with open(filename, mode="r", encoding="UTF8") as f:
        return json.load(f)