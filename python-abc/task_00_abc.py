#!/usr/bin/python3
"""Creating abstract classes"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Defining Animal class"""
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return ("Bark")


class Cat(Animal):
    def sound(self):
        return ("Meow")
