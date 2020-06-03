#!/usr/bin/python3
import sys


save_json = __import__('7-save_to_json_file').save_to_json_file
load_json = __import__('8-load_from_json_file').load_from_json_file
loaded = []
try:
    loaded = load_json("add_item.json")
except FileNotFoundError:
    args = list(sys.argv)[1:]
    save_json(str(args), "add_item.json")
args = list(sys.argv)[1:]
loaded += args
save_json(loaded, "add_item.json")
