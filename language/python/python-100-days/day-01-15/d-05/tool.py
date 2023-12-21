# !/usr/bin/env python
# coding= utf-8
'''
Author         : yum <richardminyu@foxmail.com>
Date           : 2023-01-20 23:15:14
LastEditors    : yum <richardminyu@foxmail.com>
LastEditTime   : 2023-12-10 20:01:04
Description    :

'''

def get_true_factor(n):
    """_获取素数的真因子_

    Args:
        n (_int_): _素数_

    Returns:
        _int_: _素数的真因子_
    """
    if n <= 1 or int(n) != n:
        return []

    factor_list = []
    sum = 0

    for x in range(1, int(n / 2) + 1):
        if n % x == 0:
            factor_list.append(x)

    for y in factor_list:
        sum += y

    if sum == n:
        return factor_list


def is_perfect_number(n):
    """_判断一个数是否是完全数/完备数_

    Args:
        n (_int_): _一个整数_

    Returns:
        _boolean_: _description_
    """
    if n <= 1 or int(n) != n:
        return False

    factor_list = []
    sum = 0

    for x in range(1, int(n / 2) + 1):
        if n % x == 0:
            factor_list.append(x)

    for y in factor_list:
        sum += y

    if sum == n:
        return True


def is_prime(n):
    """_素数判定_

    Args:
        n (_int_): _被判定的正整数_

    Returns:
        _boolean_: _是否素数_
    """
    # 过滤输入参数
    if n <= 1 or int(n) != n:
        return False

    is_prime = True

    for x in range(2, int(n / 2) + 1):
        if n % x == 0:
            is_prime = False
            break

    return True if (is_prime and n != 1) else False


if __name__ == '__main__':
    print(get_true_factor(6))
    print(get_true_factor(28))
    print(get_true_factor(496))
    print(get_true_factor(8128))
    print(get_true_factor(33550336))
