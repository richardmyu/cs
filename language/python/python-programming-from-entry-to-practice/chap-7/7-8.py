# -*- coding: utf-8 -*-

sandwich_orders = ['a', 'b', 'c', 'd', 'e']
finihed_sandwich = []

while sandwich_orders:
    for val in sandwich_orders:
        print(f'I made you {val} sandwich')

        finihed_sandwich.append(val)
        sandwich_orders.remove(val)

print(f'finihed sandwich {finihed_sandwich}')
