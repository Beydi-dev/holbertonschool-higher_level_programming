#!/usr/bin/python3
"""
Provides a single function `matrix_divided`
that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides elements of a matrix (ints, floats) by div, rounded to 2 decimals.

    Args:
        matrix (list of lists): Matrix of integers/floats
        div (int or float): The divisor

    Raises:
        TypeError: If matrix is not a list of lists of ints or floats
        TypeError: If each row of the matrix is not of the same size
        TypeError: If div is not a number (int or float)
        ZeroDivisionError: If div is equal to 0

    Returns:
        New matrix with all elements divided by div, rounded to 2 decimals
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list)
                                               for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_lengths = [len(row) for row in matrix]
    if len(set(row_lengths)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(num / div, 2) for num in row]
        for row in matrix
    ]
