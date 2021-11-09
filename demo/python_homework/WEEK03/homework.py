# -*- coding: utf-8 -*-

# 1.求正整数 n 以内中 3 和 5 的倍数之和
def mul_sum(n):
    res = 0
    for i in range(3, n):
        if i % 3 == 0:
            res += i
        elif i % 5 == 0:
            res += i
        else:
            continue
    return res


print(mul_sum(3))  # 0
print(mul_sum(5))  # 3
print(mul_sum(6))  # 8
print(mul_sum(10))  # 23
