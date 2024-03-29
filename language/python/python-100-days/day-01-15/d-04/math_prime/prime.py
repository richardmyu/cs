# !/usr/bin/env python
# coding= utf-8
'''
Author         : yum <richardminyu@foxmail.com>
Date           : 2023-01-18 23:16:07
LastEditors    : yum <richardminyu@foxmail.com>
LastEditTime   : 2023-12-10 19:56:23
Description    : 素数判定
'''


def is_prime(n):
    '''_素数判定_

    Args:
        n (_int_): _被判定的正整数_

    Returns:
        _boolean_: _是否素数_
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
