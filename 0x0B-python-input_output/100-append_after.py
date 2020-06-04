#!/usr/bin/python3
""" append_after module """


def append_after(filename="", search_string="", new_string=""):
    """ append a line just after the search string was founded """
    with open(filename, mode="r+", encoding="UTF8") as f:
        nline = 0
        new_list = []
        for line in f:
            new_list.append(line)
            line = line.split()
            for word in line:
                if word == search_string:
                    new_list.append(new_string)
            nline += 1
        new_list = "".join(new_list)
    with open(filename, mode="w", encoding="UTF8") as f:
        f.write(new_list)
