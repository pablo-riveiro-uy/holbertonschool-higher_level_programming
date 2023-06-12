#!/usr/bin/python3
""" Contains a class for a Sqare """
""" Contains a class for a Sqare """


class Square:
    """ Defines a Sqare, still not"""

    def __init__(self, __size=0):
        """ Asigning a private atribute to self __size"""
        if not isinstance(__size, int):
            raise TypeError('size must be an integer')
        if int(__size) < 0:
            raise TypeError('size must be >= 0')
        self.__size = __size
    pass
