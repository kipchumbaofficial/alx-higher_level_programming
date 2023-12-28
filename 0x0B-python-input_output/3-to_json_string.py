#!/usr/bin/python3
"""
JSON serialization/encoding function
"""
import json


def to_json_string(my_obj):
    """JSON encoding"""
    return json.dumps(my_obj)
