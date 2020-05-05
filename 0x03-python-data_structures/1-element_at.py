#!/usr/bin/python3

def element_at(my_list, idx):
    """ return the idx element of the list """
    if idx < 0 or idx >= len(my_list):
        return -1
    return my_list[idx]