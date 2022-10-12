# -*- coding: utf-8 -*-

from collections import OrderedDict

keys_info = OrderedDict()
keys_info['list'] = 'a date structure'
keys_info['dict'] = 'a date structure'
keys_info['for'] = 'looping structure'
keys_info['while'] = 'looping structure'
keys_info['if'] = 'branched structure'

for key, val in keys_info.items():
    print(f'{key}: {val}')
