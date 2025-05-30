#!/usr/bin/python3
"""Module 11-square
Defines a Square class that inherits from Rectangle.
"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represents a square using Rectangle as base."""

    def __init__(self, size):
        """Initialize square with size (width = height = size)."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the square description."""
        return f"[Square] {self.__size}/{self.__size}"

