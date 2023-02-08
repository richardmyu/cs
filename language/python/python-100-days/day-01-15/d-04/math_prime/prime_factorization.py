'''
@Time: 2023/01/19 11:11:52
@Author: yum
@Email: richardminyu@foxmail.com
@File: prime_factorization.py

分解质因数
'''

from prime import is_prime


def factorise_prime(n):
    '''_分解质因数_

    Args:
        n (_int_): _被分解正整数_

    Returns:
        _list_: _因子列表_
    '''
    # 过滤输入参数
    if n <= 1 or int(n) != n:
        return

    # 排除本身是素数
    if is_prime(n):
        return [1, n]

    prime_list = []

    for x in range(2, int(n / 2) + 1):
        if n % x == 0 and is_prime(x):
            prime_list.append(x)
            di = n / x

            while di % x == 0:
                prime_list.append(x)
                di /= x

    return prime_list
