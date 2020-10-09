# -*- coding: utf-8 -*-

import json

numbers = [2, 3, 5, 7, 11, 13]
filename = "number.json"

"""
json.dump(data, file) 
    1.第一个参数：要存储的数据
    2.第二个参数：可存储数据的文件对象
"""

with open(filename, 'w') as file_obj:
    json.dump(numbers, file_obj)
