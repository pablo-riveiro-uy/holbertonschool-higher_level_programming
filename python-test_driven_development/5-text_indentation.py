#!/usr/bin/python3
"""_summary_

"""


def text_indentation(text):
    """_summary_

    Args:
        text (_type_): _description_

    Raises:
        TypeError: _description_
    """
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    enter = False
    separators = ['.', '?', ':']
    for letter in text:
        if letter == " " and enter:
            continue
        enter = False
        if letter not in separators:
            print(letter, end="")
        else:
            print(letter)
            print()
            enter = True
