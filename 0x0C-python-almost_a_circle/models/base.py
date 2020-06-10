#!/usr/bin/python3
""" Base module """
import json
import csv


class Base:
    """ Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ id models constructor """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert a dictionarie into string
        this function is used as a complement of
        to_dictionary method to store the current obj state
        into a json file
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """ convert a json reprentation into a
        python object. Usefull to read json files
        """
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save a obj or objs into a json file """
        new_list = []

        with open(cls.__name__+".json", mode="w", encoding="UTF8") as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ used to save an obj or some obj into a csv file """
        doc = cls.__name__+".csv"
        with open(doc, mode="w", encoding="UTF8", newline='') as f:
            writer = csv.writer(f)
            if list_objs is None:
                writer.writerow([])
            else:
                for obj in list_objs:
                    if cls.__name__ == "Rectangle":
                        writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
                    else:
                        writer.writerow(
                            [obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """ load an obj from a csv file """
        doc = cls.__name__+".csv"
        with open(doc, mode="r", encoding="UTF8", newline='') as f:
            csv_reader = csv.reader(f)
            instances = []
            keys = {}
            for obj in csv_reader:
                if cls.__name__ == "Rectangle":
                    keys["width"] = int(obj[1])
                    keys["height"] = int(obj[2])
                    keys["x"] = int(obj[3])
                    keys["y"] = int(obj[4])
                    keys["id"] = int(obj[0])
                    instances.append(cls.create(**keys))
                else:
                    keys["size"] = int(obj[1])
                    keys["x"] = int(obj[2])
                    keys["y"] = int(obj[3])
                    keys["id"] = int(obj[0])
                    instances.append(cls.create(**keys))
            return instances

    @classmethod
    def create(cls, **dictionary):
        """ create an instance from a dictionary
        or an argument list. Usually when you recover
        an obj from a csv or json file, you first get
        a dictionary or a list, this function is usefull
        to load the last instances
        """
        arg = []
        if cls.__name__ == "Rectangle":
            keys = ["id", "width", "height", "x", "y"]
        else:
            keys = ["id", "size", "x", "y"]
        for key in keys:
            if dictionary.get(key) is not None:
                arg.append(dictionary[key])
        new = cls(1, 1)
        new.update(*arg)
        return new

    @classmethod
    def load_from_file(cls):
        """ recover an obj from a json file """
        try:
            with open(cls.__name__+".json", mode="r", encoding="UTF8") as f:
                instances = []
                json = cls.from_json_string(f.read())
                for obj in json:
                    instances.append(cls.create(**obj))
                return instances
        except FileNotFoundError:
            return []
