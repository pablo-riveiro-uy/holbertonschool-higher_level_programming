#!/usr/bin/python3
str = "{}"
for char in range(97, 123):
    if char != 101 and char != 113:
        print(str.format(chr(char)), end='')
