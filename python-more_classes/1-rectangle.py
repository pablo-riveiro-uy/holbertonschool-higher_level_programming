#!/usr/bin/python3
"""_summary_
    """


class Rectangle():
    """_summary_
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self._Rectangle__width = width
        if not isinstance(height, int):
            raise TypeError('width must be an integer')
        if height < 0:
            raise ValueError('width must be >= 0')
        self._Rectangle__height = height

    @property
    def width(self):
        return self._Rectangle__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._Rectangle__width = value

    @property
    def height(self):
        return self._Rectangle__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self._Rectangle__height = value

    pass
