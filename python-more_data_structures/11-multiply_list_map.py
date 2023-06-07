#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    if my_list and number:
        new_list = my_list.copy()

        new_list = map(lambda x: x*number, my_list)
        return list(new_list)
