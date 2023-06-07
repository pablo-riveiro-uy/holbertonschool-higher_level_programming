#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sorted_data = sorted(a_dictionary.keys())
        for x in sorted_data:
            print("{}: {}".format(x, a_dictionary.get(x)))
