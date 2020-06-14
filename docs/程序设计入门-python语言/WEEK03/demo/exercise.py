# -*- coding: utf-8 -*-

import math

# # 二分法求(算数)平方根
# x = float(input("Enter the number "))
# if x < 1:
#     print("please enter the number")
#     x = float(input("Enter the number "))
# low = 0
# high = x
# guess = (low + high) / 2
#
# while abs(guess ** 2 - x) > 1e-5:
#     if guess ** 2 < x:
#         low = guess
#     else:
#         high = guess
#     guess = (low + high) / 2
# print("The root of x is ", guess)

# x < 0 无解，是因为，负数的平方恒大于负数，即 high = guess 恒成立；

# x < 1 无解：是因为在(0,1)区间内，guess 只会无限接近 x，而 x**2 < x 恒成立，即 low = guess 恒成立；

# 素数
# num = int(input("Enter the number "))

# for i in range(2, num):
#     # 怎么优化？
#     if num % i == 0:
#         print("The number is not a prime")
#         break
# else:
#     print("The number is a prime")
#
# for i in range(2, int(math.sqrt(num)) + 1):
#     # 怎么优化？
#     # 只选择素数来检验
#     if num % i == 0:
#         print("The number is not a prime")
#         break
# else:
#     print("The number is a prime")

# 回文数
h = int(input("Enter the number: "))
h_temp = h
h_prime = 0

while h_temp != 0:
    # print(h_prime, h_temp)
    h_prime = h_prime * 10 + h_temp % 10
    h_temp //= 10

if h == h_prime:
    print("the number is a palindrome")
else:
    print("the number is not a palindrome")
