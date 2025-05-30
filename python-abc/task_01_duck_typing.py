#!/usr/bin/env python3
"""Shapes, Interfaces, and Duck Typing"""

from abc import ABC, abstractmethod
from math import pi

class Shape(ABC):
    """class that represent the shape"""

    @abstractmethod
    def area(self):
        """define the area"""
        pass

    @abstractmethod
    def perimeter(self):
        """define the perimeter"""
        pass

class Circle(Shape):
    """class that represent this circle"""

    def __init__(self, radius):
        """define radius of this circle"""
        self.radius = radius

    def area(self):
        """define area of this circle"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """define perimeter of this circle"""
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    """class that represent this circle"""

    def __init__(self, width, height):
        """define the width and the height of this rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """define area of this rectangle"""
        return self.width * self.height

    def perimeter(self):
        """define perimeter of this rectangle"""
        return 2 * (self.width + self.height)

def shape_info(shape):
    """display the information of the shape"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
