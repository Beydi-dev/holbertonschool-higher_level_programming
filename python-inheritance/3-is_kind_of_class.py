#!/usr/bin/python3
"""Checks if an object is an instance of a specified class."""


def is_kind_of_class(obj, a_class):
    """True if object is an instance of a class
    or class that inherited from, False otherwise"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
