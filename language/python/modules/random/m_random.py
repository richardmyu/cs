'''
random
方法返回一个随机数，
它在半开区间 [0,1) 范围内，
包含 0 但不包含 1。
'''

import random

# [0, 1)
print(random.random())

# [0, 10)
print(random.random() * 10)
