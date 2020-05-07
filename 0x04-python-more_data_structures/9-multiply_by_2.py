#!/usr/bin/python3


def multiply_by_2(a_dictionary):
    """ multiply by 2 all the values into a diccionary """
    new_dict = dict()
    for key in a_dictionary:
        new_dict.setdefault(key, a_dictionary[key] * 2)
    return new_dict
