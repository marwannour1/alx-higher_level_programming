#!/usr/bin/python3
"""This module contains the base class for all models in the application."""


class Base:
    """This class is the base class for all models in the application."""
    __nb_objects = 0

    def __init__(self, id=None):
        """This method initializes a new instance of the Base class."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """This method returns the JSON string representation of a list of
        dictionaries."""
        import json
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """This method writes the JSON string representation of a list of
        objects to a file."""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """This method returns the list of the JSON string representation."""
        import json
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """This method returns an instance with all attributes already set."""
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        elif cls.__name__ == "Square":
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """This method returns a list of instances."""
        import os
        filename = cls.__name__ + ".json"

        if not os.path.exists(filename):
            return []

        with open(filename, "r") as f:
            list_dicts = cls.from_json_string(f.read())

        return [cls.create(**d) for d in list_dicts]
