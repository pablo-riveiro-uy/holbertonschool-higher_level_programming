#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    if b < 0:
        a = 1 / a
        b *= -1
    base = a
    for i in range(1, b):
        if a < 0:
            a *= -1
        a = base * a
    return a
