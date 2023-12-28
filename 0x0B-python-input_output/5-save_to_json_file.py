#!/usr/bin/python3
'''
JSON dumps
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    dumping to a file
    '''

    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(json.dumps(my_obj)))
