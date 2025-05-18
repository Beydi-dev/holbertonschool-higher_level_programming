#!/usr/bin/python3
"""
This module provides a single function `add_integer` that adds two numbers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats after casting floats to integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The integer sum of a and b after casting.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)