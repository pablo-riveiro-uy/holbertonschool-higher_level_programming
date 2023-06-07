#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    new_list = my_list.copy()
    def mult(n, number):
        n * number
    map(mult(number), new_list)
    