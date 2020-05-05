#!/usr/bin/python3


def print_list_integer(my_list=[]):
    """ Print elements into a list followed by a new line """
    for i in range(0, len(my_list)):
        print("{:d}".format(my_list[i]))
