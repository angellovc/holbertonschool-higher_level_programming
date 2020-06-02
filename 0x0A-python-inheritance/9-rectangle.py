#!/usr/bin/python3
""" this is a Rectangle class module"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class"""
    def __init__(self, width, height):
        """initialize width and height values
        Arguments:
            width {[int]}
            height {[int]}
        """
        super().integer_validator(width, width)
        super().integer_validator(height, height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """Return a printable element refered to the area of the Rectangle class
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """Return the area of the rectangle class"""
        return self.__width * self.__height
