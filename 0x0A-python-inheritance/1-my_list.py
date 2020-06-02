#!/usr/bin/python3
"""[MyList class module]"""


class MyList(list):
    """[it Inherit from list the ability to make list and his methods]
    Arguments:
        list {[list class]}
    """
    def print_sorted(self):
        """[this method print the list in a sorted way]
        """
        sorted = self.copy()
        sorted.sort()
        print(sorted)
