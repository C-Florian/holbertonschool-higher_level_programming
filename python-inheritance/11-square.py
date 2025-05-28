#!/usr/bin/python3
"""Square #2"""

Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
        """class Square that inherits from Rectangle"""

    def __init__(self, size):
        """initialize square"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """define the area of square"""
        return self.__size ** 2

    def __str__(self):
        """describe the square"""
        return f"[Square] {self.__size}/{self.__size}"

