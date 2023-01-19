# -*- coding: utf-8 -*-

'''
@Time: 2023/01/19 11:11:52
@Author: yum
@Email: richardminyu@foxmail.com
@File: prime-factor.py

分解质因数
'''

import math
import prime


def decomposition_prime_factor(n):
    if n <= 1 or int(n) != n:
        return void

    prime_list = []

    for x in range(2, n):
        while n % x == 0 and prime.check_prime(n):
            prime_list.append(x)
            n = x

    return prime_list
