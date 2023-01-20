# -*- coding: utf-8 -*-

'''
@Time: 2023/01/18 23:11:57
@Author: yum
@Email: richardminyu@foxmail.com
@File: gcd.py

最大公约数常见集中方法的实现
--质因数分解法
--欧几里得算法（辗转相除法）
--更相减损法
--短除法
'''

import math
from prime import n_is_prime
from comprime import n_m_is_comprime

##############
#  #
##############
def gcd_prime_1(a, b):
    """_质因数分解法 1 —— 找出两个数的公约数，只取最大的一个公约数_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _int_: _最大公约数_
    """
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif n_is_prime(a) and n_is_prime(b):
        return 1
    else:
        di = 2
        end = int((max(a, b) / 2))

        for x in range(end + 1, 2, -1):
            if a % x == 0 and b % x == 0 and x > di:
                di = x

        return di


def gcd_prime_2(a, b):
    """_质因数分解法 2 —— 找出两个数的公约数列表，取两个列表的交集子元素自乘_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _int_: _最大公约数_
    """
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif n_is_prime(a) and n_is_prime(b):
        return 1
    else:
        a_dict = {}
        b_dict = {}
        intersect = []
        multiple = 1

        # 分别获取 a b 的质因子，放入字典
        for x in range(2, int(max(a, b) / 2) + 1):
            if a % x == 0 and n_is_prime(x):
                a_dict[x] = 1
                di_a = a / x

                while di_a % x == 0:
                    a_dict[x] += 1
                    di_a /= x

            if b % x == 0 and n_is_prime(x):
                b_dict[x] = 1
                di_b = b / x

                while di_b % x == 0:
                    b_dict[x] += 1
                    di_b /= x

        # 计数单个因子出现次数
        count = 1

        # 遍历字典，获取出现在两个字典中的因子及其个数
        for key, value in a_dict.items():
            if key in b_dict.keys():
                if value >= b_dict[key]:
                    count = b_dict[key]
                else:
                    count = value

                for z in range(1, count + 1):
                    intersect.append(key)

        # 因子交集
        for y in intersect:
            multiple *= y

        return multiple


def gcd_euclidean(a, b):
    """_欧几里得法_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _int_: _最大公约数_
    """
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif n_is_prime(a) and n_is_prime(b):
        return 1
    else:
        if a > b:
            a, b = b, a

        di = 1

        while b % a != 0:
            di = b % a
            a, b = di, a

        return di


def gcd_reduce(a, b):
    """_更相减损法_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _int_: _最大公约数_
    """
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif n_is_prime(a) and n_is_prime(b):
        return 1
    else:
        if a > b:
            a, b = b, a

        count = 0

        # 如果都是偶数，先用 2 约简
        while a % 2 == 0 and b % 2 == 0:
            a = int(a / 2)
            b = int(b / 2)
            count += 1

        # 先计算一次差
        di = b - a

        while a != di:
            if a > di:
                # 减数大于差
                # == new_di = a - di
                # == a = di di = new_di = a - di
                a, di = di, a - di
            else:
                a, di = a, di - a

        return di * math.pow(2, count)


def gcd_division(a, b):
    """_短除法_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _int_: _最大公约数_
    """
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif n_m_is_comprime(a, b):
        # 互质
        return 1
    else:
        # 非互质
        end = int(max(a, b) / 2) + 1
        prime_list = []
        di = 1
        x = 2

        while not n_m_is_comprime(a, b) and x < end:
            if a % x == 0 and b % x == 0:
                prime_list.append(x)
                a = int(a / x)
                b = int(b / x)
            else:
                x += 1

        for z in prime_list:
            di *= z

        return di
