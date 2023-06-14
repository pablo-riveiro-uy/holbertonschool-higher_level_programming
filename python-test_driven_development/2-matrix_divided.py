#!/usr/bin/python3
""" Module to divide a Matrix"""


def matrix_divided(matrix, div):
    """ Function to divide a matrix"""
    row_size = len(matrix[0])
    for a_list in matrix:
        if not isinstance(a_list, list):
            raise TypeError(
                'matrix must be a matrix (list of lists) of integers/floats')
        if not len(a_list) == row_size:
            raise TypeError('Each row of the matrix must have the same size')
        for number in a_list:
            if not isinstance(number, int) and isinstance(number, float):
                raise TypeError(
                    'matrix must be a matrix (list of lists) ?\
                      of integers/floats')
        if not isinstance(div, int) and not isinstance(div, float):
            raise TypeError('div must be a number')
        if div == 0:
            raise ZeroDivisionError('division by zero')

    new_list = []

    for i in matrix:
        sub_matrix = []
        for j in i:
            sub_matrix.append(round(j / div, 2))
        new_list.append(sub_matrix)
    return new_list
