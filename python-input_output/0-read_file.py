#!/usr/bin/python3
"""a function that reads a text file (UTF8) and prints it to stdout"""


def read_file(filename=""):
    """a function that reads a text file (UTF8) and prints it to stdout"""
    with open(filename) as file:
        content = file.read()
        print(content, end="")
