# -*- coding: utf-8 -*-

import math

# homework 1

# 斐波那契数列


def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        # return fib(n-1)+fib(n-2)
        i = 2
        f1 = 1
        f2 = 1
        fn = f1+f2
        while (i <= n):
            f3 = f1+f2
            fn = f3
            f1 = f2
            f2 = f3
            i = i+1
        return fn


# print(fib(1))  # 1
# print(fib(10))  # 89
# print(fib(11))  # 144
# print(fib(12))  # 233
# print(fib(13))  # 377

# 对于一个最大项值不超过 n 的斐波那契数列，求值为偶数的项的和


def filSum(n):
    result = 0
    if n < 11:
        for i in range(1, n+1):
            if fib(i) <= n:
                if fib(i) % 2 == 0:
                    result += fib(i)
            else:
                break
    else:
        for i in range(1, int(math.sqrt(n))+1):
            if fib(i) <= n:
                if fib(i) % 2 == 0:
                    result += fib(i)
            else:
                break
    return result


print(filSum(2))  # 2
print(filSum(3))  # 2
print(filSum(8))  # 10
print(filSum(100))  # 44
