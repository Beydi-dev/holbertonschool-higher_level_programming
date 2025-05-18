#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters:
    '.', '?', ':'

    Args:
        text (str): The input string

    Raises:
        TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if text == "":
        print()
        return

    buffer = ""
    for char in text:
        buffer += char
        if char in ".?:":
            print(buffer.strip())
            print()
            buffer = ""

    if buffer.strip() != "":
        print(buffer.strip())
