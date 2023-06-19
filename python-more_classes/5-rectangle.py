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
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
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
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self._Rectangle__height = value

    def area(self):
        return self._Rectangle__height * self._Rectangle__width

    def perimeter(self):
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return 0
        return self._Rectangle__height * 2 + self._Rectangle__width * 2

    def __str__(self):
        if self._Rectangle__height == 0 or self._Rectangle__height == 0:
            return ""
        else:
            return "\n".join("#" * self.width for i in range(self.height))

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")

    pass
