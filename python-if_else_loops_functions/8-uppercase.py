#!/usr/bin/env python3
def uppercase(str):
    for i in range(0, len(str)):
        ordinal = ord(str[i])
        if ordinal > 96 and ordinal < 123:
            ordinal = ordinal - 32
        print("{}".format(chr(ordinal)), end="")
    print()
