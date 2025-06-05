#!/usr/bin/python3
"""this module does basic serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """this function serializes and saves to a file"""
    with open(filename, "w") as f:
        json.dump(data, f)
    pass


def load_and_deserialize(filename):
    """this function desarializes to recreate a dictionary"""
    with open(filename) as f:
        data = json.load(f)
        return data
    pass
