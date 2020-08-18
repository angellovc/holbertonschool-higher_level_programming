#!/usr/bin/python3
""" find_peak module """


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    list_of_integers.sort()
    if list_of_integers:
        return list_of_integers[-1]
    else:
        return None
