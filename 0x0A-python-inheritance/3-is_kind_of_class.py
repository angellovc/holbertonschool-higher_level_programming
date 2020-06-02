#!/usr/bin/python3
"""is_kind_of_class function module"""


def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of a_class or inherit it from
    Arguments:
        obj {[instance]}
        a_class {[instance]}

    Returns:
        True in case obj is instance or inherit from a_class, False in failure
    """
    return isinstance(obj, a_class)
