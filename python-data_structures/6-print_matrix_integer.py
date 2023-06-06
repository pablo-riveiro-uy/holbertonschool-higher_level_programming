#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        try:
            matrix[1]
            for i in range(len(matrix)):
                for j in range(0, len(matrix[i]) - 1):
                    print("{:d}".format(matrix[i][j]), end=' ')
                print("{:d}".format(matrix[i][j] + 1))
        except IndexError:
            print()
