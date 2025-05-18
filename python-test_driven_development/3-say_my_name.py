#!/usr/bin/python3
"""
This is the "3-say_my_name" module
It coutains the function:
say_my_name
"""


def say_my_name(first_name, last_name=""):
    """
    Prints first name and last name

    Args:
        first_name: first name
        last_name: last name

    Raises:
        TypeError: If first_name and /or last_name are not strings

    Returns:
    My name is <first name> <last name>
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
