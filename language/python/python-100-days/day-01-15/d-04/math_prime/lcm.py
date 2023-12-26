# !/usr/bin/env python
# coding= utf-8
'''
Author         : yum <richardminyu@foxmail.com>
Date           : 2023-01-18 23:14:14
LastEditors    : yum <richardminyu@foxmail.com>
LastEditTime   : 2023-12-26 22:02:18
Description    : 最小公倍数常见集中方法的实现
                     --质因数分解法
                     --公式法
'''
from prime import is_prime
from comprime import is_comprime
from gcd import gcd_prime_1


def lcm_prime(a, b):
    '''_质因数分解法 —— 将两数 a,b 因式分解，获取其中 b 中 a 没有的因子，与 a 相乘，即可得最小公倍数_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _int_: _最小公倍数_
    '''
    if a % b == 0:
        return a
    elif b % a == 0:
        return b
    elif is_comprime(a, b):
        return a * b
    else:
        a_dict = {}
        b_dict = {}
        multiple = 1

        # 分别获取 a b 的质因子，放入字典
        for x in range(2, int(max(a, b) / 2) + 1):
            if a % x == 0 and is_prime(x):
                a_dict[x] = 1
                di_a = a / x

                while di_a % x == 0:
                    a_dict[x] += 1
                    di_a /= x

            if b % x == 0 and is_prime(x):
                b_dict[x] = 1
                di_b = b / x

                while di_b % x == 0:
                    b_dict[x] += 1
                    di_b /= x

        # 遍历字典，获取 a 独有的质因子或缺少的公有质因子
        for key, value in a_dict.items():
            if key not in b_dict.keys():
                multiple *= key**value
            elif key in b_dict.keys() and value > b_dict[key]:
                multiple *= key ** (value - b_dict[key])

        # 将 a 独有的质因子或缺少的公有质因子乘 b
        multiple *= b
        return int(multiple)


def lcm_formula(a, b):
    '''_公式法 —— 获取最大公约数，被两数之积除，即为最小公倍数_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _int_: _最小公倍数_
    '''
    if a % b == 0:
        return a
    elif b % a == 0:
        return b
    elif is_comprime(a, b):
        return a * b
    else:
        multiple = 1
        di = gcd_prime_1(a, b)
        multiple = int(a * b / di)
        return multiple


def lcm_division(a, b):
    '''_短除法_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _int_: _最小公倍数_
    '''
    if a % b == 0:
        return a
    elif b % a == 0:
        return b
    elif is_comprime(a, b):
        # 互质
        return a * b
    else:
        # 非互质
        end = int(max(a, b) / 2) + 1
        prime_list = []
        di = 1
        x = 2

        while not is_comprime(a, b) and x < end:
            if a % x == 0 and b % x == 0:
                prime_list.append(x)
                a = int(a / x)
                b = int(b / x)
            else:
                x += 1

        for z in prime_list:
            di *= z

        di = di * a * b
        return di
