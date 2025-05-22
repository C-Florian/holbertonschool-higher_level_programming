#!/usr/bin/python3
"""Module 6-square
Defines a Square class with size and position, area calculation, and printing.
"""

class Square:
    """Class that defines a square with size and position attributes."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with size and position.

        Args:
            size (int): The size of the square.
            position (tuple): Tuple of 2 positive integers for printing position.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size with validation.

        Args:
            value (int): Size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for position with validation.

        Args:
            value (tuple): Tuple of
