#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if my_list and idx:
        if idx < 0 or idx > len(my_list):
            return my_list
        my_list.remove(idx)
        return my_list
