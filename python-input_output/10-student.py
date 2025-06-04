#!/usr/bin/python3
"""student to JSON with filter"""

class Student:
    """class that defines a student by attributes"""


    def __init__(self, first_name, last_name, age):
        """
        initializes a new Student instance

        args:
            first_name (str): student first name
            last_name (str): student last name
            age (int): student age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns a dictionary that store the student attributes

        if `attrs` is a list of strings, only the attributes listed
        will be returned (if they exist)

        args:
            attrs (list, optional): list of attribute names to include
        
        return:
            dict: filtered or full dictionary of student attributes
        """
        if isinstance(attrs, list) and all(type(attr) == str for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
