#!/usr/bin/python3
""" MyInt class module """


class MyInt(int):
    """ Use __eq__ magic method to change the behavoir of
    the comparison between number stored in MyInt against number
    passed through
        int {[int]} -- [This is the number to compare]
    """
    def __eq__(self, number):
        return False

    def __ne__(self, other):
        return not self.__eq__(other)
