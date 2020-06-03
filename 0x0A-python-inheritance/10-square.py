#!/usr/bin/python3
""" Square class module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Make a new Square object using the Rectangle constructor
    Arguments:
        Rectangle {[int]} -- [Represent the size of Square]
    """
    def __init__(self, size):
        """ Initialize square usging rectangle constructor """
        Rectangle.__init__(self, size, size)
