# -*- coding: utf-8 -*-

keys_info = {
    'list': 'a date structure',
    'dict': 'a date structure',
    'for': 'looping structure',
    'while': 'looping structure',
    'if': 'branched structure',
}

for key, val in keys_info.items():
    print(f'{key}: {val}')

keys_info['append'] = 'a function'
keys_info['insert'] = 'a function'
keys_info['pop'] = 'a function'
keys_info['sort'] = 'a function'
keys_info['sorted'] = 'a function'

for key, val in keys_info.items():
    print(f'{key}: {val}')
