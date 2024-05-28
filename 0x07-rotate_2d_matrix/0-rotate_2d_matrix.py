#!/usr/bin/python3
"""Function to Rotate 2D Matrixs"""


def reverse_matrix(matrix):
    """function for reversing matrix"""
    for row in matrix:
        row.reverse()


def transpose_matrix(matrix, n):
    """Function for transposing matrix"""
    for x in range(n):
        for y in range(x, n):
            matrix[x][y], matrix[y][x] = matrix[y][x], matrix[x][y]


def rotate_2d_matrix(matrix):
    """Function for rotating 2d matrix"""
    n = len(matrix)
    transpose_matrix(matrix, n)
    reverse_matrix(matrix)
    return matrix
