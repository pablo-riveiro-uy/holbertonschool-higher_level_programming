#!/usr/bin/python3
""" Contains a class for a Sqare """


class Square:
    """ Defines a Sqare and get a position"""

    def __init__(self, __size=0, __position=(0, 0)):
        self.__size = __size
        self.__position = __position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """ Asigning a private atribute to self size"""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if int(value) < 0:
            raise TypeError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """ Take a position to thw sqare"""
        if not isinstance(value, tuple):
            raise TypeError('position must be a tuple of 2 positive integers')
        for t in value:
            if not isinstance(t, int):
                raise TypeError(
                    'position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        """ Printing the sqare on size given"""
        if self.__size == 0:
            print("")
        else:
            spaces = self.position[1]
            while spaces > 0:
                print()
                spaces -= 1
            for i in range(self.size):
                for p in range(self.__position[0]):
                    print(" ", end="")
                for j in range(self.size - 1):
                    print("#", end="")
                print("#")

    def area(self):
        """ Calc area of a sqaare of given size"""
        return pow(self.__size, 2)
