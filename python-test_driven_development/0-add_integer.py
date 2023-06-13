#!/usr/bin/python3
def add_integer(a, b=98):
    """
    >>>(add_integer(1, 2)
    3
    >>>add_integer(100, -2)
    98
    >>>add_integer(100.3, -2)
    100
    >>>add_integer(2)
    98
    >>>add_integer(4, "School")
    b must be an integer
    >>>add_integer(None))
    a must be an integer
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
    