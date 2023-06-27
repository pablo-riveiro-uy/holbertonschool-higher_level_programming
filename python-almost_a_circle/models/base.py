#!/usr/bin/python3
"""_summary_
    """
import json


class Base:
    """_summary_
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """_summary_

        Args:
            id (_type_, optional): _description_. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ _summary_ """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """_summary_ """

        cls.list_objs = list_objs

        if not list_objs:
            with open("emptylist.json", 'w') as f:
                f.write(Base.to_json_string([]))
            return

        if type(list_objs[0] == "Rectangle"):
            filename = "Rectangle.json"
        else:
            filename = "Square.json"

        with open(filename, 'w') as f:
            for obj in list_objs:
                to_dict = obj.to_dictionary()
                f.write(Base.to_json_string(to_dict))
