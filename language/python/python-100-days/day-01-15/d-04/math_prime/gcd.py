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

import math
import prime

##############
# 质因数分解法 #
##############
def gcd_prime_1(a, b):
    """_找出两个数的公约数，只取最大的一个公约数_

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
    elif prime.n_is_prime(a) and prime.n_is_prime(b):
        return 1
    else:
        divisor = 2
        end = int((max(a, b) / 2))

        for x in range(2, end + 1):
            if a % x == 0 and b % x == 0 and x > divisor:
                divisor = x

        return divisor


def gcd_prime_2(a, b):
    """_找出两个数的公约数列表，取两个列表的交集子元素自乘_

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
    elif prime.n_is_prime(a) and prime.n_is_prime(b):
        return 1
    else:
        a_list = []
        b_list = []
        multiple = 1

        # 分别获取 a b 的约数因子
        for x in range(2, int(max(a, b) / 2) + 1):
            if a % x == 0 and prime.n_is_prime(x):
                a_list.append(x)
                di_a = a / x

                while di_a % x == 0:
                    a_list.append(x)
                    di_a /= x

            if b % x == 0 and prime.n_is_prime(x):
                b_list.append(x)
                di_b = b / x

                while di_b % x == 0:
                    b_list.append(x)
                    di_b /= x
        # TODO set 去重了
        # 不如换成对象，属性记录值，值记录数量
        intersect = list(set(a_list) & set(b_list))

        for y in intersect:
            multiple *= y

        return multiple


##############
#  辗转相除法  #
##############
def gcd_2(a, b):
    """_summary_

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
    elif prime.n_is_prime(a) and prime.n_is_prime(b):
        return 1
    else:
        divisor = 2
        end = int(max(a, b) / 2)

        for x in range(2, end + 1):
            if a % x == 0 and b % x == 0 and x > divisor:
                divisor = x

        return divisor


##############
#  更相减损法  #
##############
def gcd_3(a, b):
    """_summary_

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
    elif prime.n_is_prime(a) and prime.n_is_prime(b):
        return 1
    else:
        divisor = 2
        end = int(max(a, b) / 2)
        for x in range(2, end + 1):
            if a % x == 0 and b % x == 0 and x > divisor:
                divisor = x

        return divisor


##############
#   短除法   #
##############
def gcd_4(a, b):
    """_summary_

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
    elif prime.n_is_prime(a) and prime.n_is_prime(b):
        return 1
    else:
        divisor = 2
        end = int(max(a, b) / 2)
        for x in range(2, end + 1):
            if a % x == 0 and b % x == 0 and x > divisor:
                divisor = x

        return divisor


if __name__ == '__main__':
    print(gcd_prime_2(2, 3), 1)
    print(gcd_prime_2(2, 4), 2)
    print(gcd_prime_2(2, 5), 1)
    print(gcd_prime_2(12, 3), 3)
    print(gcd_prime_2(12, 18), 6)
    print(gcd_prime_2(14, 21), 7)
    print(gcd_prime_2(144, 180), 36)
