#!/usr/bin/python3
"""_summary_
    """


def read_file(filename=""):
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read())


"""_summary_

    Args:
        filename (str, optional): _description_. Defaults to "".
    """
