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

    start = 0
    for i in range(len(text)):
        if text[i] in ".?:":
            print(text[start:i + 1].strip())
            print()
            start = i + 1
            while start < len(text) and text[start] == ' ':
                start += 1
    if start < len(text):
        print(text[start:].strip())
