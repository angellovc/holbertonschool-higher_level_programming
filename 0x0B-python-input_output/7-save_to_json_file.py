#!/usr/bin/python3
""" sate_to_json_file module """
import json


def save_to_json_file(my_obj, filename):
    """ save the json obj into a json file """
    with open(filename, mode="w", encoding="UTF8") as f:
        json.dump(my_obj, f)
