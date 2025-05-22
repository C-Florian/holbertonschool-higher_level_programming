#!/usr/bin/python3
"""Module 4-square
Defines a class Square with size property, validation, and area computation.
"""

class Square:
    """Class that defines a square by its size."""

    def __init__(self, size=0):
        """
        Initialize the square with a given size.

        Args:
            size (int): The size of the square. Must be an integer >= 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for the size attribute.

        Returns:
            int: The current
