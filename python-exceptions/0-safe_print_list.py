#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        index = x
    except KeyError:
        return my_list[i]
    for i in my_list[0:index]:
        print("{}".format(i), end="")
    print()
    return my_list[i - 1]
