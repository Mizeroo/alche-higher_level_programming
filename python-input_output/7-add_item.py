#!/usr/bin/python3
"""Script  adds arguments to  Python list saved as JSON."""
import json
import os
import sys

filename = "add_item.json"

if os.path.exists(filename):
    with open(filename, "r", encoding="utf-8") as f:
        my_list = json.load(f)
else:
    my_list = []

my_list.extend(sys.argv[1:])

with open(filename, "w", encoding="utf-8") as f:
    json.dump(my_list, f)
