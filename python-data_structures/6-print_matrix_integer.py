#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    try:
        matrix[1]
        c = 0
        for i in matrix:
            for j in i:
                c += 1
                if (c != 3):
                    print('{} '.format(j), end="")
                else:
                    c = 0
                    print('{}'.format(j))
    except IndexError:
        print()
