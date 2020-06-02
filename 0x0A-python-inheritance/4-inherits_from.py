#!/usr/bin/python3
"""inherits_from function module"""


def inherits_from(obj, a_class):
    """Check if object inherit from a_class
    if obj is same as a_class it means that obj not inherit from a_class
    due to both are equals
    Arguments:
        obj {[object]}
        a_class {[class]}
    Returns:
        True if object inherit from, False if don't
    """
    if type(obj) == a_class:
        return False
    return isinstance(obj, a_class)
