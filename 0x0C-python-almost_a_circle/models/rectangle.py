#!/usr/bin/python3
""" Rectangle class module """
from models.base import Base


class Rectangle(Base):
    """ This is a Rectangle class
    Args:
        Base (class): [inherit id from class]
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ rectangle width getter """
        return self.__width

    @width.setter
    def width(self, width):
        """ rectangle widht setter """
        if type(width) != int:
            errors("no_integer", "width")
        if width <= 0:
            errors("zero_or_negative", "width")
        self.__width = width

    @property
    def height(self):
        """ rectangle height getter """
        return self.__height

    @height.setter
    def height(self, height):
        """ rectangle height setter """
        if type(height) != int:
            errors("no_integer", "height")
        if height <= 0:
            errors("zero_or_negative", "height")
        self.__height = height

    @property
    def x(self):
        """ rectangle axis x getter """
        return self.__x

    @x.setter
    def x(self, x):
        """ rectangle axis x getter """
        if type(x) != int:
            errors("no_integer", "x")
        if x < 0:
            errors("negative", "x")
        self.__x = x

    @property
    def y(self):
        """ rectangle axis y getter """
        return self.__y

    @y.setter
    def y(self, y):
        """ rectangle axis y setter """
        if type(y) != int:
            errors("no_integer", "y")
        if y < 0:
            errors("negative", "y")
        self.__y = y

    def area(self):
        """ represent the rectangle area of the instance """
        return self.width * self.height

    def display(self):
        """ show a rectangle on the screen based on his properties
            x, y axis
            weidht, height
        """
        print('\n' * self.y, end="")
        for row in range(0, self.height):
            print(" " * self.x, end="")
            print("#" * self.width, end="")
            print("")

    def __str__(self):
        """ Return a string representation of rectangle instance """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(
            self.id, self.x, self.y, self.width, self.height)

    def update(self, *args, **kwargs):
        """ update values usually used to return
        informations from json files
        """
        if args:
            keys = ["id", "width", "height", "x", "y"][0:len(args)]
            for value, key in zip(args, keys):
                setattr(self, key, value)
        else:
            for key in kwargs:
                setattr(self, key, kwargs[key])

    def to_dictionary(self):
        """ get the current state of rectangle instance into a dictionary """
        keys = ["id", "width", "height", "x", "y"]
        dic = {}
        for key in keys:
            dic[key] = getattr(self, key)
        return dic


def errors(error, variable=""):
    """ module errors """
    if error == "no_integer":
        raise TypeError("{} must be an integer".format(variable))
    if error == "zero_or_negative":
        raise ValueError("{} must be > 0".format(variable))
    if error == "negative":
        raise ValueError("{} must be >= 0".format(variable))
