#!/usr/bin/python3
""" rectangle class module """


class Rectangle:
    """
    Rectangle

    Attributes:
        width: only receive integers and positive numbers
        height: only receive integers and positive numbers
    """
    def __init__(self, width_value, height_value):
        self.width = width_value
        self.height = height_value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            errors("width_no_integer")
        if value < 0:
            errors("width_negative")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            errors("height_no_integer")
        if value < 0:
            errors("height_negative")
        self.__height = value


def errors(error):
    # width errors
    if error == "width_no_integer":
        raise TypeError("width must be an integer")
    if error == "width_negative":
        raise ValueError("width must be >= 0")
    # height errors
    if error == "height_no_integer":
        raise TypeError("height must be an integer")
    if error == "height_negative":
        raise ValueError("height must be >= 0")
