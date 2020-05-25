#!/usr/bin/python3
""" class Rectangle module """


class Rectangle:
    """
    Rectangle

    Attributes:
        number_of_instances:
        print_symbol
        width: only receive integers and positive numbers
        height: only receive integers and positive numbers

    Methods:
        area: get the area of the rectangle
        perimeter: get the perimeter of the rectangle
        str: print the rectangle using #
        repr: return a representation of Rectangle class
        del: delete an instance
        bigger_or_equal: get the bigget Rectangle instance based on his areas
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

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
            return rectangle
        for row in range(0, self.height):
            for colunm in range(0, self.width):
                rectangle += str(self.print_symbol)
            if row != self.height - 1:
                rectangle += '\n'
        return rectangle

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2


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
