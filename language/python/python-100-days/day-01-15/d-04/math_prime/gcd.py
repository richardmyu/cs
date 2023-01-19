# -*- coding: utf-8 -*-

'''
@Time: 2023/01/18 23:11:57
@Author: yum
@Email: richardminyu@foxmail.com
@File: gcd.py

最大公约数常见集中方法的实现
--质因数分解法
--辗转相除法
--更相减损法
--短除法
'''


def gcd(a, b):
    """质因数分解法"""
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    else:
        divisor = 2
        end = int(math.sqrt(max(a, b)))
        for x in range(2, end + 1):
            if a % x == 0 and b % x == 0 and x > divisor:
                divisor = x

        return divisor


def gcd_2(a, b):
    """辗转相除法"""
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    else:
        divisor = 2
        end = int(math.sqrt(max(a, b)))
        for x in range(2, end + 1):
            if a % x == 0 and b % x == 0 and x > divisor:
                divisor = x

        return divisor
