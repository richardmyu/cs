# -*- coding: utf-8 -*-

# 强制类型

# int
print(int(0))
# 0
print(int(123))
# 123
print(int(1.23))
# 1
print(int(0x123))
# 291
# print(int(''))
# ValueError: invalid literal for int() with base 10: ''
print(int('123'))
# 123
# print(int('11hello'))
# ValueError: invalid literal for int() with base 10: '11hello'
print(int(True))
# 1
# print(int(1 + 2j))
# TypeError: can't convert complex to int

# str
print(str(0))
# '0'
print(str(123))
# '123'
print(str(1.23))
# '1.23'
print(str(0x123))
# '291'
print(str(''))
# ''
print(str('123'))
# '123'
print(str('11hello'))
# '11hello'
print(str(True))
# 'True'
print(str(1 + 2j))
# print(type(str(1 + 2j)))
# '(1+2j)'

# float
print(float(0))
# 0.0
print(float(123))
# 123.0
print(float(1.23))
# 1.23
print(float(0x123))
# 291.0
# print(float(''))
# ValueError: could not convert string to float: ''
print(float('123'))
# 123.0
# print(float('11hello'))
# ValueError: could not convert string to float: '11hello'
print(float(True))
# 1.0
# print(float(1 + 2j))
# TypeError: can't convert complex to float

# bool
print(bool(0))
# False
print(bool(123))
# True
print(bool(0.23))
# True
print(bool(0x123))
# True
print(bool(''))
# False
print(bool('123'))
# True
print(bool('11hello'))
# True
print(bool(True))
# True
print(bool(1 + 2j))
# True
