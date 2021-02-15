# -*- coding: utf-8 -*-

my_list = [5, "he", "she", 7]
my_list_num = [1, 4, 3, 6]
my_list_str = ['apple', 'carrot', 'banana', 'mango']

# []
print(my_list[0])
# 5

# [:]
print(my_list[1:3])
# ['he', 'she']

# +
print(my_list + ["it"])
# [5, "he", "she", 7, 'it']
print(my_list)
# [5, "he", "she", 7]

# *
print(my_list[0] * 2)
# 555
print(my_list[2] * 2)
# sheshe

# in
print('he' in my_list)
# True
print('He' in my_list)
# False

# len
print(len(my_list))
# 4

# for
for i in my_list:
    print(i)
# 5
# he
# she
# 7

my_list.append('hello')
print(my_list)

my_list.extend(['world'])
print(my_list)

print('-------')
try:
    my_list.sort()
except TypeError:
    print('字符类型不能与数字类型进行比较')
else:
    print('ok')

my_list_str.sort()
my_list_num.sort()
print(my_list)
print(my_list_num)
print(my_list_str)

print(my_list)
del my_list[-1]
print(my_list)
