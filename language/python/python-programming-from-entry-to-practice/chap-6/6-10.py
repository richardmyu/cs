# -*- coding: utf-8 -*-

minions = {
    'bob': [1, 5, 9],
    'Kvein': [2, 3],
    'stuart': [3, 6, 9],
    'admin': [4],
    'superadmin': [0],
}

for name, nums in minions.items():
    if len(nums) > 1:
        print(f'{name} like nubmer are {nums}')
    else:
        print(f'{name} favorite nubmer is {nums}')
