#!/usr/bin/python3
"""pascal's Triangle"""

def pascal_triangle(n):
    """
    Generates the Pascal’s triangle of n rows.

    Each row represents a level in Pascal's Triangle,
    where each number is the sum of the two directly above it.

    Args:
        n (int): The number of rows to generate.

    Returns:
        list: A list of lists, where each sub-list represents a row in the triangle.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for j in range(1, len(prev_row)):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)
        triangle.append(new_row)

    return triangle

