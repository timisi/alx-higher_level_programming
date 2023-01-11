#!/usr/bin/python3
"""
This module provides from_json_string() function
"""
import json


def from_json_string(my_str):
    """
    This is a function that returns an object represented by JSON string

    Args:
        param1 (my_str): JSON representation
    """
    return json.loads(my_str)
