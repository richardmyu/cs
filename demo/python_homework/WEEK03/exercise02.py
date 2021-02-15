# -*- coding: utf-8 -*-

import math

# 素数
num = int(input("Enter the number "))

for i in range(2, num):
    # 怎么优化？
    if num % i == 0:
        print("The number is not a prime")
        break
else:
    print("The number is a prime")

for i in range(2, int(math.sqrt(num)) + 1):
    # 怎么优化？
    # 只选择素数来检验
    if num % i == 0:
        print("The number is not a prime")
        break
else:
    print("The number is a prime")
