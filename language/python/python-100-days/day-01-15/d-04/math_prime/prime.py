# -*- coding: utf-8 -*-

'''
@Time: 2023/01/18 23:16:10
@Author: yum
@Email: richardminyu@foxmail.com
@File: prime.py

素数判定
'''

import math


def check_prime(num):
    """_素数判定_

    Args:
        num (_int_): _被判定的正整数_

    Returns:
        _boolean_: _是否素数_
    """
    end = int(math.sqrt(num))
    is_prime = True

    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break

    is_prime = True if (is_prime and num != 1) else False

    return is_prime
