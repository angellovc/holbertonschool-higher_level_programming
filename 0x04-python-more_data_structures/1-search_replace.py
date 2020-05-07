#!/usr/bin/python3


def chnge(old, new):
    def change_item(item):
        if item == old:
            item = new
        return item
    return change_item


def search_replace(my_list, search, replace):
    change = chnge(search, replace)
    return list(map(change, my_list))
