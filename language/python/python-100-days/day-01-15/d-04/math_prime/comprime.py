# -*- coding: utf-8 -*-

'''
@Time: 2023/01/20 19:22:16
@Author: yum
@Email: richardminyu@foxmail.com
@File: comprime.py

判断两个正整数是否互质
'''


def n_m_is_comprime(a, b):
    """_判断两个正整数是否互质_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _boolean_: _是否互质_
    """
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
