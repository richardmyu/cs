# -*- coding: utf-8 -*-
import json

filename = 'number.json'

"""
json.load(file):

"""
with open(filename) as file_obj:
    numbers = json.load(file_obj)
print(numbers)
