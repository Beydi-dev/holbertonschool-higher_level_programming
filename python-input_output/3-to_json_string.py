#!/usr/bin/python3
import json
"""The JSON representation of an object (string)"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)"""
    res = json.dumps(my_obj)
    return res
