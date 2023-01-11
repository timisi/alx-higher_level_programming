#!/usr/bin/python3
"""
This module provides to_json_string() function
"""
import json


def to_json_string(my_obj):
    """
    This is a function that returns the JSON representation of an object

    Args:
        param1 (my_obj): object to be parsed
    """
    return json.dumps(my_obj)
