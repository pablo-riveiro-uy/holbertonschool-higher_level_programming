#!/usr/bin/python3
for a in range(0, 10):
    for b in range(0, 10):
        if b > a:
            if a == 8 and b == 9:
                print(f'{a}{b}')
            else:
                print(f'{a}{b}, ', end='')
