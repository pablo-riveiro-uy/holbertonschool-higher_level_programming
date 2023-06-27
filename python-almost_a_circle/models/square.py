#!/usr/bin/python3
"""_summary_"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """_summary_

    Args:
        Rectangle (_type_): _description_
    """

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(width=size, height=size, x=x, y=y, id=id)

        def __str__(self):
            """_summary_

            Returns:
                _type_: _description_
            """
            txt = "[Square] ({}) {}/{} - {}"
            return txt.format(self.id, self.x, self.y, self.size)
