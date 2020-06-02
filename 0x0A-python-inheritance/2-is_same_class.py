#!/usr/bin/python3
"""[is_same_class function module]"""


def is_same_class(obj, a_class):
    """[check if object is from the same class as a_class]
    Arguments:
        obj -- [any object]
        a_class -- [any kind of class]

    Returns:
        True if both are equals, False in failure
    """
    if type(obj) == a_class:
        return True
    return False
