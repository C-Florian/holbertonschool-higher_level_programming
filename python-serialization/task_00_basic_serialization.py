#!/usr/bin/python3

"""
task_00_basic_serialization.py
"""

import json

def serialize_and_save_to_file(data, filename):
    """
    serialize a Python dictionary and save it to a JSON file

    args:
    data (dict): The dictionary to serialize
    filename (str): The name of the file to save the JSON data
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file)

def load_and_deserialize(filename):
    """
    load and deserialize JSON data from a file into a Python dictionary

    args:
    filename (str): The name of the JSON file to read

    returns:
    dict: The dictionary reconstructed from the JSON file
    """
    with open(filename, 'r') as json_file:
        return json.load(json_file)

