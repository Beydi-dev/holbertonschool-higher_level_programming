#!/usr/bin/python3
"""Serialization and deserialization using pickle module"""
import pickle


class CustomObject:
    """Custom object with name, age and student status"""

    def __init__(self, name, age, is_student):
        """Initialize the CustomObject with name, age and is_student"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Prints the attributes of the object"""
        print("Name: {}\nAge: {}\nIs Student: {}".
              format(self.name, self.age, self.is_student))

    def serialize(self, filename):
        """Serializes the object and saves it to a file"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Deserializes a CustomObject from a file and returns it"""
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            return obj
        except (FileNotFoundError, pickle.PickleError):
            return None
