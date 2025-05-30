#!/usr/bin/python3
"""Module that defines a Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size):
        """Initialize square with size.

        Args:
            size (int): size of the square (must be > 0)
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return the square description."""
        return f"[Square] {self.__size}/{self.__size}"

