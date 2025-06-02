#!/usr/bin/python3
"""Writes an Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Function writes an Object to a text file,
    using a JSON representation"""

    """Serializing json"""
    json_object = json.dumps(my_obj)

    """Writing to filename"""
    with open("filename", "w") as outfile:
        outfile.write(json_object)
