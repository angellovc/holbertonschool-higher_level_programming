#!/usr/bin/python3


def no_c(my_string):
    new_string = ""
    for i, letter in zip(range(len(my_string)), my_string):
        if letter in "Cc":
            continue
        new_string = new_string + letter
    return new_string
