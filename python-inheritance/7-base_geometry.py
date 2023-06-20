#!/usr/bin/python3
"""_summary_
"""


class BaseGeometry():
    """_summary_
    """

    def area(self):
        """_summary_
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """_summary_
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))