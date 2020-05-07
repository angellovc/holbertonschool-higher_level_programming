#!/usr/bin/python3


def common_elements(set_1, set_2):
    """ find the common elements """
    new_set = set()
    for str in set_1:
        if str in set_2:
            new_set.add(str)
    return(new_set)
