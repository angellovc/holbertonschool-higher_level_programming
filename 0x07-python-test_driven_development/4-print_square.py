#!/usr/bin/python3
""" prit_square function module """


def print_square(size):
    """
    print_square make a square from size**2 usign # insted of lines or dots

    Args:
        size: must be an integer up to zero of equial to zero

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(0, size):
        if row != 0:
            print("")
        print("#" * size, end="")  # print the columns
    print("")
