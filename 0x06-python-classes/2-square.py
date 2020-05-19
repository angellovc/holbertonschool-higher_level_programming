#!/usr/bin/python3
""" Class Square module """


class Square:
    """
    Square Class

    Attributes:
        size: represent the size of the square

    """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError('size must be an integer')
        elif size < 0:
            raise ValueError('size must be >= 0')
        self.size = size
