# -*- coding: utf-8 -*-

import math

# 4.任意正整数 n 以内有多少个循环素数
# 循环素数：循环移动数位，构成的新数均为素数
# 举例：197 --> 197，971，719


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

# 是否循环素数


def isCyclePrime(n):
    if n <= 0:
        print("输入数字有误")
        return 0
    if not isPrime(n):
        # print("请输入素数")
        return 0

    strNum = str(n)
    numLen = len(strNum)
    num = n
    isCP = True

    for i in range(numLen):
        a = num//10
        b = num % 10
        num = int(b*math.pow(10, numLen-1)+a)
        # print("---", num)
        if isPrime(int(num)):
            continue
        else:
            isCP = False
            break

    return isCP


print(isCyclePrime(197))
# print(isCyclePrime(37))
# print(isCyclePrime(23))
# print(isCyclePrime(79))

# 循环素数统计


def countCP(n):
    if n <= 1:
        print("输入数据有误")
        return 0

    count = 0
    for i in range(n):
        if isCyclePrime(i):
            # print("cycle-prime: ", i)
            count += 1

    return count


print(countCP(100))
