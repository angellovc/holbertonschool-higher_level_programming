#!/usr/bin/python3


def uniq_add(my_list=[]):
    """ sum each element of a list excluding the occurences """
    depured_list = []
    for number in my_list:  # delete the occurrences
        if number not in depured_list:
            depured_list.append(number)
    return sum(depured_list)
