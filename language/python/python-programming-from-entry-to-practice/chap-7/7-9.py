# -*- coding: utf-8 -*-

sandwich_orders = ['a', 'pastrami', 'c', 'pastrami', 'pastrami']
finihed_sandwich = []

print("No pastrami")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    for val in sandwich_orders:
        print(f'I made you {val} sandwich')

        finihed_sandwich.append(val)
        sandwich_orders.remove(val)

if "pastrami" not in finihed_sandwich:
    print(f'finihed sandwich {finihed_sandwich}')
