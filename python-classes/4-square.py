#!/usr/bin/python3
"""This module defines a Square class with size validation and area method."""


class Square:
    """Represents a square with size and methods to get area."""

    def __init__(self, size=0):
        """Initialize a Square with an optional size (default is 0)."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square with validation.

        Args:
            value (int): Size of the square, must be >= 0

        Raises:
            TypeError: If value is not an integer
            ValueError: If value is negative
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square
        """
        return self.__size ** 2

