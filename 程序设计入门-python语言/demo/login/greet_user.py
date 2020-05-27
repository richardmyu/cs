# -*- coding: utf-8 -*-
import json

filename = "data/username.json"

try:
    with open(filename) as f_obj:
        username = json.load(f_obj)
except FileNotFoundError:
    pass
else:
    print("Welcome back, " + username + '!')
