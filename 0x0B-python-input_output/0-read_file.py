#!/usr/bin/python3
""" read_file modeule fuction """


def read_file(filename=""):
    """Read a text file and print the content inside of
    Keyword Arguments:
        filename {str} -- file name and his path
    """
    with open(filename, mode="r", encoding="UTF8") as f:
        print(f.read(), end="")
