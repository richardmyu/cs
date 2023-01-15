# -*- coding: utf-8 -*-

import json

filename = 'number.json'

try:
    with open(filename) as f_obj:
        num = json.load(f_obj)

        print(f'I know your favorite number! It\'s {num}')
except FileNotFoundError:
    num = int(input("Enter the number your like: "))

    with open(filename, 'w') as f_obj:
        json.dump(num, f_obj)
