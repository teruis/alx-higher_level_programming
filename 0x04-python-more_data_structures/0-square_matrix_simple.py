#!/usr/bin/python3
"""
Module that computes the square value of all integers of a matrix
"""


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix

    Args:
        matrix (list[list]): 2D matrix of integers

    Returns:
        list[list]: a new matrix with each integer squared
    """
    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(num ** 2)
        new_matrix.append(new_row)
    return (new_matrix)
