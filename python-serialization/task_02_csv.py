#!/usr/bin/env python3
"""
task_02_csv.py
"""

import csv
import json

def convert_csv_to_json(csv_filename):
    """
    convert data from a CSV file to a JSON file named 'data.json'

    args:
    csv_filename (str): the path to the CSV file

    returns:
    bool: True if the conversion was successful, False otherwise
    """
    try:
        with open(csv_filename, 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            data = list(reader)

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)

        return True
    except Exception:
        return False

