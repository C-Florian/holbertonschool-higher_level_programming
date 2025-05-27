#!/usr/bin/python3
"""function that returns the list of available attributes and methods of an object"""

def lookup(obj):
    """function that returns the list of available attributes and methods of an object

    args:
    obj: object"""
    
    return dir(obj)
