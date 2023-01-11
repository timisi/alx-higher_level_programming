#!/usr/bin/python3
"""
This module provides pascal_triangle() function
"""


def pascal_triangle(n):
    """
    This is a function that returns a list of lists of Pascal's triangle

    Args:
        param1 (n): size of the triangle

    Returns:
        a list of lists of integers representing the Pascal's triangle
    """
    if n <= 0:
        return []

    a = [[1 for i in range(1, j + 1)] for j in range(1, n + 1)]
    for i in range(2, n):
        for j in range(1, i):
            a[i][j] = a[i - 1][j - 1] + a[i - 1][j]

    return a
