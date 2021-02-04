# -*- coding: utf-8 -*-

import math


# 4.任意正整数 n 以内有多少个循环素数
# 循环素数：循环移动数位，构成的新数均为素数
# 举例：197 --> 197，971，719


# 是否素数
def is_prime(n):
    counter = 0
    for i in range(1, n + 1):
        if n % i == 0:
            counter += 1
        else:
            continue
    if counter == 2:
        return True
    else:
        return False


# 是否循环素数
def is_cycle_prime(n):
    if n <= 0:
        print("输入数字有误")
        return 0
    if not is_prime(n):
        # print("请输入素数")
        return 0

    str_num = str(n)
    num_len = len(str_num)
    num = n
    is_cp = True

    for i in range(num_len):
        a = num // 10
        b = num % 10
        num = int(b * math.pow(10, num_len - 1) + a)
        # print("---", num)
        if is_prime(int(num)):
            continue
        else:
            is_cp = False
            break

    return is_cp


# 循环素数统计
def count_cp(n):
    if n <= 1:
        print("输入数据有误")
        return 0

    count = 0
    for i in range(n):
        if is_cycle_prime(i):
            # print("cycle-prime: ", i)
            count += 1

    return count


print(count_cp(100))
