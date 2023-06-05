#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0:
        return my_list
    if idx > len(my_list):
        return my_list
    other_list = []
    for i in range(0, my_list[idx] - 1):
        other_list.append(my_list[i])
    other_list.append(element)
    for i in range(my_list[idx], len(my_list)):
        other_list.append(my_list[i])
    return other_list
