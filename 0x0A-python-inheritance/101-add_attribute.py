#!/usr/bin/python3
""" add attribute module """


def add_attribute(obj, key, value):
    """ check if you can add value into a class """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    obj.__dict__[key] = value
