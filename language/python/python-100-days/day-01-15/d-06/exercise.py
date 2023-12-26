# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-01-21 19:38:59
Description    :
'''
from tool import is_comprime, is_prime


def cal_gcd(a, b):
    '''_最大公约数_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _int_: _参数的最大公约数_
    '''
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    elif is_prime(a) and is_prime(b):
        return 1
    else:
        di = 2
        end = int((max(a, b) / 2))

        for x in range(end + 1, 2, -1):
            if a % x == 0 and b % x == 0 and x > di:
                di = x

        return di


def cal_lcm(a, b):
    '''_最小公倍数_

    Args:
        a (_int_): _正整数_
        b (_int_): _正整数_

    Returns:
        _int_: _参数的最小公倍数_
    '''
    if a % b == 0:
        return a
    elif b % a == 0:
        return b
    elif is_comprime(a, b):
        return a * b
    else:
        multiple = 1
        di = cal_gcd(a, b)
        multiple = int(a * b / di)

        return multiple


def is_palindrome(n):
    '''_实现判断一个数是不是回文数_

    Args:
        n (_int_): _正整数_

    Returns:
        _boolean_:
    '''
    if n < 1 or int(n) != n:
        return

    # 反转 n，但不能直接操作 n
    num = n
    reversed_num = 0

    while num > 0:
        reversed_num = reversed_num * 10 + num % 10
        num //= 10

    if n == reversed_num:
        return True
    else:
        return False


def is_prime(n):
    '''_素数判定_

    Args:
        n (_int_): _正整数_

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


def is_palindrome_prime(n):
    '''_判断输入的正整数是不是回文素数_

    Args:
        n (_int_): _正整数_

    Returns:
        _boolean_:
    '''
    if is_palindrome(n) and is_prime(n):
        return True
    else:
        return False


if __name__ == '__main__':
    print(cal_gcd(12, 18), 6)
    print(cal_lcm(12, 18), 36)

    print(is_palindrome(124321), False)
    print(is_palindrome(12344321), True)
    print(is_palindrome(123454321), True)
    print(is_palindrome(12321), True)
    print(is_palindrome(1221), True)

    print(is_prime(2), True)
    print(is_prime(6), False)
    print(is_prime(9), False)
    print(is_prime(12321), False)
    print(is_prime(1221), False)

    print(is_palindrome_prime(12321), False)
    print(is_palindrome_prime(1221), False)
