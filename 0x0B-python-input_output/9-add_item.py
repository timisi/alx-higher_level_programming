#!/usr/bin/python3
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
try:
    a = load_from_json_file("add_item.json")
except Exception:
    a = []
i = 1
while i < len(sys.argv):
    a.append(sys.argv[i])
    i += 1
save_to_json_file(a, "add_item.json")
