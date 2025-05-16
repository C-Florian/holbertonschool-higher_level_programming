#!/usr/bin/python3
"""
This module defines a function to divide all elements of a matrix by a number.
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of the matrix by div and returns a new matrix.

    Args:
        matrix (list of lists): A matrix with int/float elements
        div (int or float): The divisor (non-zero)

    Returns:
        list: A new matrix with results rounded to 2 decimal places

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats
                   or rows are not the same size
                   or div is not a number
        ZeroDivisionError: If div is zero
    """
    if not isinstance(matrix, list) or matrix == [] or \
       not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_len = len(matrix[0])
    for row in matrix:
        if len(row) != row_len:
            raise TypeError("Each row of the matrix must have the same size")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(elem / div, 2) for elem in row] for row in matrix]
