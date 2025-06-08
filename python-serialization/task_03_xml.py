#!/usr/bin/env python3
"""
task_03_xml.py
"""

import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    serialize a Python dictionary into an XML file

    args:
    dictionary (dict): the dictionary to serialize
    filename (str): the name of the file to save the XML data
    """
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_from_xml(filename):
    """
    deserialize an XML file into a Python dictionary

    args:
    filename (str): the name of the XML file to read

    returns:
    dict: a dictionary containing the data from the XML file
    """
    tree = ET.parse(filename)
    root = tree.getroot()

    result = {}
    for child in root:
        result[child.tag] = child.text

    return result

