#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    add_nums = [0, 0]
    for i in range(len(tuple_a)):
        if i >= 2:
            break
        add_nums[i] += tuple_a[i]

    for i in range(len(tuple_b)):
        if i >= 2:
            break
        add_nums[i] += tuple_b[i]

    new_tuple = (add_nums[0], add_nums[1])
    return new_tuple
