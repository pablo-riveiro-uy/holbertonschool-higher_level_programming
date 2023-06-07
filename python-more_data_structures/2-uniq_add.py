#!/usr/bin/python3
def uniq_add(my_list=[]):
    add = 0
    set_nums = set(my_list)
    for i in set_nums:
        add += i
    return add
