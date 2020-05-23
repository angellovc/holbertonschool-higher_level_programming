#!/usr/bin/python3
""" say_my_name module """


def say_my_name(first_name, last_name=""):
    """
    say_my_name: display the name that you entere, just strings alloweds

    Args:
        first_name: a string is expected here
        last_name="": in case the last_name doesn't be typed in, function
        going to use the default option ""

    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
