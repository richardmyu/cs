# -*- coding: utf-8 -*-

my_tuple = (1, 'it', 'is')

print(my_tuple[0])
# 1

print(my_tuple[1:])
# ['it', 'is']

new_my_tuple = 'yes', 'no', my_tuple
print(new_my_tuple)

print(new_my_tuple[2][2])

my_empty = ()
print(my_empty)
my_single_tuple = (1,)
print(my_single_tuple)
my_single_tuple2 = (1)
print(my_single_tuple2)
