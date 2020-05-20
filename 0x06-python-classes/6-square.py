#!/usr/bin/python3
""" Class Square module """


class Square:
    """Square class
    Attributes:
        size: represent the size of square
    Methods:
        area: get the area of the square class
        size: size getter and setter
        position: position getter and setter
        my_print: print a hashtag
    """
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if type(position) != tuple:
                raise TypeError("position must be a tuple of 2 \
positive integers")
        if len(position) != 2:
                raise TypeError("position must be a tuple of 2 \
positive integers")
        self.__position = position

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size != 0:
            for new_line in range(0, self.__position[1]):
                        print("")
            for i in range(0, self.__size):
                if i != 0:
                    print("")
                for space in range(0, self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size, end="")
        print("")

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(position) != tuple:
                raise TypeError("position must be a tuple of 2 \
positive integers")
        if len(position) != 2:
                raise TypeError("position must be a tuple of 2 \
positive integers")
        self.__position = value

    @property
    def size(self):
        return int(self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
