# -*- coding: utf-8 -*-

# 1.求正整数 n 以内中 3 和 5 的倍数之和

def mulSum(n):
    res = 0
    for i in range(3, n):
        if i % 3 == 0:
            res += i
        elif i % 5 == 0:
            res += i
        else:
            continue
    return res


print(mulSum(3))  # 0
print(mulSum(5))  # 3
print(mulSum(6))  # 8
print(mulSum(10))  # 23

# 2.任意正整数 n 以内的素数和

# 是否素数


def isPrime(n):
    counter = 0
    for i in range(1, n+1):
        if n % i == 0:
            counter += 1
        else:
            continue
    if counter == 2:
        return True
    else:
        return False


# print(isPrime(1))  # False
# print(isPrime(2))  # True
# print(isPrime(3))  # True
# print(isPrime(4))  # False
# print(isPrime(6))  # False
# print(isPrime(11))  # True

# 素数和

def primeSum(n):
    res = 0
    for i in range(1, n):
        if isPrime(i):
            res += i
    return res


print(primeSum(5))  # 5
print(primeSum(10))  # 17


# 3.1901 年 1 月 1 日 至 2000 年 12 月 31 日期间共有多少周日和每月 1 号重合

# 4.任意正整数 n 以内有多少个循环素数
