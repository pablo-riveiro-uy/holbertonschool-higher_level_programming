#!/usr/bin/python3
"""add items to a list and save it in a json File"""

from sys import argv

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

file = "add_item.json"

try:
    my_obj = load_from_json_file(file)
except Exception:
    my_obj = []

if len(argv) != 1:
    for i in range(1, len(argv)):
        my_obj.append(argv[i])

save_to_json_file(my_obj, file)
