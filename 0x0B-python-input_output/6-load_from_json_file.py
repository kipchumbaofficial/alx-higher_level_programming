#!/usr/bin/python3
"""
JSON loads
"""
import json


def load_from_json_file(filename):
    """
    creates from JSON object
    """
    with open(filename, "r", encoding="utf-8") as f:
        retval = json.loads(f.read())
    return retval
