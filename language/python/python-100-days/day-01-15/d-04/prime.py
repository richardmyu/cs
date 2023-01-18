# -*- coding: utf-8 -*-

'''
@Time: 2023/01/18 23:16:10
@Author: yum
@Email: richardminyu@foxmail.com
@File: prime.py

素数判定
'''


def check_prime(num):
    """判断是不是素数"""
    end = int(math.sqrt(num))
    is_prime = True

    for x in range(2, end + 1):
        if num % x == 0:
            is_prime = False
            break

    is_prime = True if (is_prime and num != 1) else False

    return is_prime


if __name__ == '__main__':
    print(check_prime(9))
    print(check_prime(11))
    print(check_prime(2))
    print(check_prime(1))
