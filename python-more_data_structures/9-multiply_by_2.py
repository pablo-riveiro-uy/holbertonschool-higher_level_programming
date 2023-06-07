#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary:
        new_dict = {}
        for i in a_dictionary:
            new_value = a_dictionary[i] * 2
            new_dict.update({i: new_value})
        return new_dict
    elif len(a_dictionary >= 0):
        return None
    else:
        return None
