#!/usr/bin/python3
""" find_peak module """


def find_peak(list_of_integers):
    """ finds a peak in a list of unsorted integers """
    i = 0
    max_num = 0
    if list_of_integers:
        for number in list_of_integers:
            if number > max_num:
                max_num = number
        return max_num
    else:
        return None
