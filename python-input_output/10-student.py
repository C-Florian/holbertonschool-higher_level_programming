#!/usr/bin/python3
"""student to JSON with filter"""

class Student:
    """class that defines a student by attributes"""

    def __init__(self, first_name, last_name, age):
        """initialize a new student

        args:
            first_name
            last_name
            age"""
    
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
                """return a  dictionnary that store all the attribute
                if attrs was a string, return exclusively this attributes

                args:
                    attrs

                returns:
                    dict"""

        if isinstance(attrs, list) and all(type(attr) == str for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
