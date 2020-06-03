#!/usr/bin/python3
""" read_lines module """


def read_lines(filename="", nb_lines=0):
    """read and print n number of lines into a text file
    Keyword Arguments:
        filename {str} -- [text file] (default: {""})
        nb_lines {int} -- [n lines to read] (default: {0})
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        lines = 0
        for line in f:
            print(line, end="")
            lines += 1
            if nb_lines > 0 and lines >= nb_lines:
                break
