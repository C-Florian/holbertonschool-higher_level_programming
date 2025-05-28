#!/usr/bin/python3
"""Integer validator"""

class BaseGeometry:
 """function that write a class BaseGeometry (based on 5-base_geometry.py)"""

    def area(self):
        """public instance method that raises an Exception with the message area() is not implemented"""

    def integer_validator(self, name, value):
        """public instance method that validates value
        args:
        name: string
        value: value"""
                if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
