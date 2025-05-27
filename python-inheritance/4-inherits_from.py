#!/usr/bin/python3
"""Defines inherites class-checking function"""


def inherits_from(obj, a_class):
    """Checks if an object is an instance of a class that inherited
(directly or indirectly) from a specified class"""
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    else:
        return False
