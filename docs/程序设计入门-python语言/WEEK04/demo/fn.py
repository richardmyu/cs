# -*- coding: utf-8 -*-

import math


# num = int(input("Enter the number "))
# num_temp = num
# num_prime = 0
# is_palin = False
# is_Prime = False
#
# for i in range(2, int(math.sqrt(num)) + 1):
#     if num % i == 0:
#         break
# else:
#     is_palin = True
#
# while num_temp != 0:
#     # print(num_prime, num_temp)
#     num_prime = num_prime * 10 + num_temp % 10
#     num_temp //= 10
#
# if num == num_prime:
#     is_Prime = True
#
# if is_palin and is_Prime:
#     print("ok")
# else:
#     print("no")

# 函数
# 回文数函数
def is_palin(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    else:
        return True


# 素数函数
def is_prime(num):
    num_temp = num
    num_prime = 0
    while num_temp != 0:
        num_prime = num_prime * 10 + num_temp % 10
        num_temp //= 10

    if num == num_prime:
        return True
    else:
        return False


num = int(input("Enter the number "))

if is_palin(num) and is_prime(num):
    print("ok")
else:
    print("no")
