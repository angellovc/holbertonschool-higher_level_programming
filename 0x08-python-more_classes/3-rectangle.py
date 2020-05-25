#!/usr/bin/python3
""" class Rectangle module """


class Rectangle:
    """
    Rectangle

    Attributes:
        width: only receive integers and positive numbers
        height: only receive integers and positive numbers

    Methods:
        area: get the area of the rectangle
        perimeter: get the perimeter of the rectangle
        str: print the rectangle using #
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

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

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        rectangle = str()
        if self.__height == 0 or self.__width == 0:
            rectangle = ""
        for row in range(0, self.height):
            rectangle += "#" * self.width
            if row != self.height - 1:
                rectangle += '\n'
        return rectangle


def errors(error):
    """ [errors]

    Arguments:
        error {[string]} -- [error name]

    Raises:
        TypeError, ValueError
    """
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
