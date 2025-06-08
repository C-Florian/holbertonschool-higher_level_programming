#!/usr/bin/python3
"""student to disk and reload"""

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

    def to_json(self, attrs=None):
        """
        returns a dictionary representation of the student

        if `attrs` is a list of strings, only the specified
        attributes will be included

        args:
            attrs (list, optional): list of attribute names to include

        returns:
            dict: filtered or full dictionary of student attributes
        """
        if isinstance(attrs, list) and all(type(attr) == str for attr in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces attributes of the student instance using a dictionary

        args:
            json (dict): dictionary with keys as attribute names and values to assign
        """
        for key, value in json.items():
            setattr(self, key, value)

