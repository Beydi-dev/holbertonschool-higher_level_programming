#!/usr/bin/python3
"""
This module defines a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""
def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.

    Args:
        text (str): The text to print.
    Raises:
        TypeError: If text is not a string.
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

    if buffer.strip():
        print(buffer.strip())
