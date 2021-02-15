# -*- coding: utf-8 -*-

import math


# 函数
# 回文数函数
def is_palindrome(a):
    for i in range(2, int(math.sqrt(a)) + 1):
        if a % i == 0:
            return False
        else:
            return True


# 素数函数
def is_prime(b):
    n_temp = b
    n_prime = 0

    while n_temp != 0:
        n_prime = n_prime * 10 + n_temp % 10
        n_temp //= 10

    if b == n_prime:
        return True
    else:
        return False


num = int(input("Enter the Number "))

if is_palindrome(num) and is_prime(num):
    print("ok")
else:
    print("no")
