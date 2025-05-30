#!/usr/bin/python3
"""Rectangle module that inherits from BaseGeometry."""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle class, inherits from BaseGeometry."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height.

        Args:
            width (int): rectangle width (must be > 0).
            height (int): rectangle height (must be > 0).
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
