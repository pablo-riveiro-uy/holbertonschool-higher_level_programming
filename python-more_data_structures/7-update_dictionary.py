#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary and key and value:
        a_dictionary.update({key: value})
    else:
        return None
    return a_dictionary