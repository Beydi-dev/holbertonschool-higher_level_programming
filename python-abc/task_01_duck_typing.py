#!/usr/bin/python3
"""Creating abstract classes"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape class with two abstract methods"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """class that inherits from Shape"""
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """class that inheirts from Shape"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


def shape_info(obj):
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
