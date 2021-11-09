# -*- coding: utf-8 -*-

# 2.任意正整数 n 以内的素数和

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


# 素数和
def prime_sum(n):
    res = 0
    for i in range(1, n):
        if is_prime(i):
            res += i
    return res


print(prime_sum(5))  # 5
print(prime_sum(10))  # 17
