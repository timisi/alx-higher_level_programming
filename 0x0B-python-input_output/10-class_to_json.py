#!/usr/bin/python3
"""
This module provides class_to_json() function
"""


def class_to_json(obj):
    """
    This is a functions that returns the dictionary description

    Args:
        param1 (obj): this object is an instance of the class
    """
    items = {}
    for attribute, value in sorted(obj.__dict__.items()):
        items[attribute] = value

    return items
