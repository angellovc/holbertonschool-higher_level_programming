#!/usr/bin/python3
""" append_after module """


def append_after(filename="", search_string="", new_string=""):
    """ append a line just after the search string was founded """
    with open(filename, mode="r", encoding="UTF8") as f:
        new_line = ""
        for line in f:
            if search_string in line:
                new_line += line + new_string
            else:
                new_line += line
    with open(filename, mode="w", encoding="UTF8") as f:
        f.write(new_line)
