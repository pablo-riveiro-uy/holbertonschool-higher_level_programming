#!/usr/bin/python3
for n in range(0, 100):
    if n < 10:
        n = f"0{n}"
    if n == 99:
        print(n)
    else:
        print('{}, '.format(n), end='')

