#!/usr/bin/python3
""" Contains a class for a Sqare """


class Square:
    """ Defines a Sqare, still not"""

    def __init__(self, __size=0):
        self.__size = __size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ Asigning a private atribute to self __size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if int(value) < 0:
            raise TypeError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Calc area of a sqaare of given size"""
        return pow(self.__size, 2)
    pass
