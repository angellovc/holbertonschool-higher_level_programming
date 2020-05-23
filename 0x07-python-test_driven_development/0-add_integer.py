#!/usr/bin/python3
""" add_integer module """


def add_integer(a, b=98):
    """
    add_integer - make a sum of two integers

    Args:
        a: need to be an integer
        b=98: need to be an integer, if no one parameter are typed in
        it will 98 the default option

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return a + b
