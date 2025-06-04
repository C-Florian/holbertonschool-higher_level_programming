#!/usr/bin/python3
"""student to JSON"""

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

        return:
            dict: attibutes of the student object
        """
        return self.__dict__

