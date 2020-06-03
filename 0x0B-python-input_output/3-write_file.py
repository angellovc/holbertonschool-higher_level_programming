#!/usr/bin/python3
"""" write_file module """


def write_file(filename="", text=""):
    """write a text into a file
    Keyword Arguments:
        filename {str} -- [file name] (default: {""})
        text {str} -- [text] (default: {""})
    Returns:
        [int] -- [number of characters writed]
    """
    with open(filename, mode="w", encoding="UTF8") as f:
        return f.write(text)
