#!/usr/bin/python3
""" Square class Module """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Square Class """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(
            self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        if args:
            keys = ["id", "size", "x", "y"][0:len(args)]
            for value, key in zip(args, keys):
                if key == "size":
                    setattr(self, "width", value)
                    setattr(self, "height", value)
                else:
                    setattr(self, key, value)
        else:
            for key in kwargs:
                if key == "size":
                    setattr(self, "width", kwargs[key])
                    setattr(self, "height", kwargs[key])
                else:
                    setattr(self, key, kwargs[key])

    def to_dictionary(self):
        keys = ["id", "width", "x", "y"]
        dic = {}
        for key in keys:
            if key == "width":
                dic["size"] = getattr(self, key)
            else:
                dic[key] = getattr(self, key)
        return dic
