#!/usr/bin/python3
def print_last_digit(number):
    last = number
    if last < 0:
        last =  last *-1
    last = last % 10
    print("{}".format(last), end="")
    return last
