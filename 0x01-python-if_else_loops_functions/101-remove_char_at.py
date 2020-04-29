#!/usr/bin/python3
""" make a copy of a string removin a letter


not in python way, but in C way
"""


def remove_char_at(str, n):
    i = 0
    new = ""
    for word, i in zip(str, range(0, len(str))):
        if i == n:
            continue
        new = new + word
    return new
