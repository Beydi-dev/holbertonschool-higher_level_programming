#!/usr/bin/python3
"""The object representation of a JSON"""
import json


def from_json_string(my_string):
    """Returns the object representation of a JSON"""
    res = json.loads(my_string)
    return res
