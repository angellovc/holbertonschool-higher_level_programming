#!/usr/bin/python3
""" class Student module """


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """json obj"""
        filtered = {}
        dic = self.__dict__
        for key in dic:
            if attrs is None or key in attrs:
                filtered[key] = dic[key]
        return filtered
