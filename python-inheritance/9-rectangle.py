#!/usr/bin/python3
"""Rectangle module with area and str methods."""


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

    def area(self):
        """Return the area of the rectangle."""
        return self.__width * self.__height

    def __str__(self):
        """Return the rectangle description."""
        return f"[Rectangle] {self.__width}/{self.__height}"

