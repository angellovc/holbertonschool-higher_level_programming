#!/usr/bin/python3
""" class to json module """


def class_to_json(obj):
    """ convert a class into json obj """
    return obj.__dict__
