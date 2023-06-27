#!/usr/bin/python3
"""_summary_"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_ """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    def __str__(self):
        txt = "[Square] ({}) {}/{} - {}"
        return txt.format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        return self.height

    @size.setter
    def size(self, value):
        self.update(width=value, height=value, size=value)

    def update(self, *args, **kwargs):
        """_summary_
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.width = value
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value
