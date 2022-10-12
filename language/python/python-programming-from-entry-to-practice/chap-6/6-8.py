# -*- coding: utf-8 -*-

bob = {'type': 'cat', 'master': 'jack'}
Kvein = {'type': 'dog', 'master': 'jack'}
stuart = {'type': 'pig', 'master': 'jack'}

pets = [bob, Kvein, stuart]

for pet in pets:
    for name, val in pet.items():
        print(f'{name} -- {val}')
