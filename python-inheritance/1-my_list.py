#!/usr/bin/python3
"""Module that defines MyList class"""


class MyList(list):
    """class that inherits from list"""
    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
