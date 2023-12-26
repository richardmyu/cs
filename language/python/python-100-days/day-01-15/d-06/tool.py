# !/usr/bin/env python
# coding= utf-8
'''
Author         : yum <richardminyu@foxmail.com>
Date           : 2023-01-21 21:17:39
LastEditors    : yum <richardminyu@foxmail.com>
LastEditTime   : 2023-12-10 20:01:39
Description    :
'''


def is_prime(n):
    '''_素数判定_

    Args:
        n (_int_): _被判定的正整数_

    Returns:
        _boolean_:
    '''
    # 过滤输入参数
    if n <= 1 or int(n) != n:
        return False

    is_prime = True

    for x in range(2, int(n / 2) + 1):
        if n % x == 0:
            is_prime = False
            break

    return True if (is_prime and n != 1) else False


def is_comprime(a, b):
    '''_判断两个正整数是否互质_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _boolean_:
    '''
    # 过滤输入参数
    if a < 1 or int(a) != a or b < 1 or int(b) != b:
        return False

    if a == 1 or b == 1:
        return True

    is_comprime = True

    for x in range(2, int(max(a, b) / 2) + 1):
        if a % x == 0 and b % x == 0:
            is_comprime = False
            break

    return is_comprime
