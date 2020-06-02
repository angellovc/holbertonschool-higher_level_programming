#!/usr/bin/python3
"""Basegeometry class module"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """area not implementet yet"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """check if the value gived is an integer
        Arguments:
            name {[string]}
            value {[int]}
        Raises:
            TypeError and ValueError
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
