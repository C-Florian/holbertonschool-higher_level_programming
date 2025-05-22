#!/usr/bin/python3
"""Module 1-square
Defines a class Square with a private instance attribute.
"""

class Square:
    """Class that defines a square by its size."""

    def __init__(self, size):
        """
        Initialize the square with a given size.

        Args:
            size (int): The size of the square (no type/value verification).
        """
        self.__size = size
