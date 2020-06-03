#!/usr/bin/python3
""" number_of_lines function module """


def number_of_lines(filename=""):
    """Get the numbers of lines into a text file
    Keyword Arguments:
        filename {str} -- [text file]
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        lines = 0
        for line in f:
            lines += 1
        return lines
