#!/usr/bin/python3
""" function that returns True if the object is exactly an instance of the specified class otherwise False"""
def is_same_class(obj, a_class):
    """function that returns True if the object is exactly an instance of the specified class ; otherwise False

    args:
    obj: object
    a_class: class"""
    return type(obj) is a_class
