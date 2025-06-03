#!/usr/bin/python3
""" write to a file"""

def write_file(filename="", text=""):
    """Writes a string to a text file and returns the number of characters written."""
    
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
