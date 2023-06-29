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
            list_dictionaries = []

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """_summary_ """

        if not list_objs or len(list_objs) == 0:
            list_objs = []

        filename = "Rectangle.json" if cls.__name__ == "Rectangle" else "Square.json"

        a_list = []

        for obj in list_objs:
            a_list.append(obj.to_dictionary())
        

        with open(filename, 'w') as f:
            a_string = Base.to_json_string(a_list)
            f.write(a_string)
    
    @staticmethod
    def from_json_string(json_string):
        """_summary_ """
        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """_summary_"""
        cls.dictionary = dictionary

        dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
        dummy.update(**dictionary)
        return dummy
    
    @classmethod
    def load_from_file(cls):
        """_summary_

        Returns:
            _type_: _description_
        """
        filename  = cls.__name__ + '.json'

        my_list = []
        try:
            with open(filename, 'r') as f:
                data = f.read()
        except FileNotFoundError:
            return []
        
        strgDAta = cls.from_json_string(data)

        for instance in range(len(strgDAta)):
            my_list.append(cls.create(**strgDAta[instance]))

        return my_list
