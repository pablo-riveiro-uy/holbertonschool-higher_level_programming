#!/usr/bin/python3
"""_summary_

    Returns:
        _type_: _description_
    """


class Student:
    """_summary_
    """

    def __init__(self, first_name, last_name, age):
        """_summary_

        Args:
            first_name (_type_): _description_
            last_name (_type_): _description_
            age (_type_): _description_
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """_summary_

        Returns:
            _type_: _description_
        """
        if attrs is None:
            return self.__dict__
        data = {}
        for at in attrs:
            if at == "first_name":
                data.update({at: self.first_name})
            elif at == "last_name":
                data.update({at: self.last_name})
            elif at == "age":
                data.update({at: self.age})

        keys = list(data.keys())

        keys.sort()
        sorted_dict = {}
        for key in keys:
            sorted_dict.update({key: data[key]})

        return sorted_dict
