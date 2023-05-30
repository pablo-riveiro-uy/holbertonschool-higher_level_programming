#!/usr/bin/env python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) > 96 and ord(str[i]) < 123:
            character = ord(str[i]) - 32
        else:
            character = ord(str[i])
        print('{}'.format(chr(character)), end='')
    print()
