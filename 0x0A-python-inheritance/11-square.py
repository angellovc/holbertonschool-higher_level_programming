#!/usr/bin/python3
""" Square class module """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class """
    def __init__(self, size):
        """ initialize width and height values
        Arguments:
            size {[int]}
        """
        super().integer_validator("height", size)
        super().__init__(size, size)
        self.__width = size
        self.__height = size

    def area(self):
        """ get the area of the square """
        return self.__width * self.__height

    def __str__(self):
        """ Return a printable element refered 
        to the area of the Square class
        """
        return "[Square] {}/{}".format(self.__width, self.__height)
