# -*- coding: utf-8 -*-

'''
@Time: 2023/01/18 23:16:10
@Author: yum
@Email: richardminyu@foxmail.com
@File: prime.py

素数判定
'''

import math


def n_is_prime(n):
    """_素数判定_

    Args:
        n (_int_): _被判定的正整数_

    Returns:
        _boolean_: _是否素数_
    """
    # 过滤输入参数
    if n <= 1 or int(n) != n:
        return False

    # 指定循环截止点
    end = int(math.sqrt(n))
    is_prime = True

    for x in range(2, end + 1):
        if n % x == 0:
            is_prime = False
            break

    return True if (is_prime and n != 1) else False
