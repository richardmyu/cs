# -*- coding: utf-8 -*-

my_dict = {
    'a': 'study',
    'b': 'work',
    'c': 'eat and drink'
}

print(my_dict['a'])

print(len(my_dict))

print('b' in my_dict)  # True
print('B' in my_dict)  # False

for d in my_dict:
    print(d, my_dict[d])

print(my_dict.items())
# dict_items([('a', 123), ('b', 456), ('c_class', 789)])

print(my_dict.keys())
# dict_keys(['a', 'b', 'c_class'])

print(my_dict.values())
# dict_values([123, 456, 789])

# print(my_dict.clear())  # None
# print(my_dict)  # {}

del my_dict['c']
print(my_dict)
