#!/usr/bin/python3
"""
task_01_pickle.py
"""

import pickle

class CustomObject:
    """
    a class representing a custom object with name, age, and student status
    """

    def __init__(self, name, age, is_student):
        """
        initialize a new CustomObject

        args:
        name (str): name of the person
        age (int): age of the person
        is_student (bool): whether the person is a student
        """
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """
        display the attributes of the object in a formatted way
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        serialize the object and save it to a file

        args:
        filename (str): the name of the file to save the object to
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        deserialize a CustomObject from a file

        args:
        filename (str): the name of the file to load the object from

        returns:
        CustomObject: the deserialized object or None if failed
        """
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None

