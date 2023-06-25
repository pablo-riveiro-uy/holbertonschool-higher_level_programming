#!/usr/bin/python3
"""_summary_
"""


def pascal_triangle(n):
    """_summary_

    Args:
        n (_type_): _description_

    Returns:
        _type_: _description_
    """
    a_list = []

    for y in range(n):
        a_list.append([1])
        for x in range(y):
            if x == y - 1:
                a_list[y].append(1)
            else:
                num = a_list[y - 1][x + 1] + a_list[y - 1][x]
                a_list[y].append(num)

    return a_list
