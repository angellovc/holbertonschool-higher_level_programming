#!/usr/bin/python3
"""" append_write module """


def append_write(filename="", text=""):
    """write a text into a file
    The text will be append at the end of the file
    Keyword Arguments:
        filename {str} -- [file name] (default: {""})
        text {str} -- [text] (default: {""})
    Returns:
        [int] -- [number of characters writed]
    """
    with open(filename, mode="a", encoding="UTF8") as f:
        return f.write(text)
