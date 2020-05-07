#!/usr/bin/python3


def best_score(a_dictionary):
    """ return the biggest value number into a dictionary """
    if not a_dictionary:
        return None
    key, value = list(a_dictionary.keys()), list(a_dictionary.values())
    key = key[value.index(max(value))]
    return key
