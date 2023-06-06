#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if set_1 and set_2:
        differents = set_1 - set_2
        differents.update(set_2 - set_1)

        return differents
