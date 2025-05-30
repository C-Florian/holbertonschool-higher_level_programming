#!/usr/bin/python3
"""Integer validator"""

class BaseGeometry:
 """function that write a class BaseGeometry"""

    def area(self):
        """public instance method that raises an Exception with a message"""
        raise Exception("area() is not implemented")


    def integer_validator(self, name, value):
        """public instance method that validates value
        args:
        name: string
        value: value"""
                if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
