#!/usr/bin/python3
"""
This module defines a function that returns the maximum integer in a list.
"""

def max_integer(list=[]):
    """
    Returns the maximum integer in a list.

    Args:
        list (list): List of integers.

    Returns:
        int: The maximum integer in the list, or None if the list is empty.
    """
    if len(list) == 0:
        return None

    max_val = list[0]
    for i in range(1, len(list)):
        if list[i] > max_val:
            max_val = list[i]
    return max_val
