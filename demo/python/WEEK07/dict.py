# -*- coding: utf-8 -*-

my_dict = {'a': 123, 'b': 456, 'c': 789}

print(my_dict['a'])

# len
print(len(my_dict))

# in
print('b' in my_dict)
print('B' in my_dict)

# for
for d in my_dict:
    print(d, my_dict[d])

# items
print(my_dict.items())

# keys
print(my_dict.keys())

# values
print(my_dict.values())

# clear
print(my_dict.clear())
print(my_dict)
