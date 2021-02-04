# -*- coding: utf-8 -*-

import math

# # 二分法求(算数)平方根
x = float(input("Enter the number "))
if x < 1:
    print("please enter the number")
    x = float(input("Enter the number "))
low = 0
high = x
guess = (low + high) / 2

while abs(guess ** 2 - x) > 1e-5:
    if guess ** 2 < x:
        low = guess
    else:
        high = guess
    guess = (low + high) / 2
print("The root of x is ", guess)

# x < 0 无解，是因为，负数的平方恒大于负数，即 high = guess 恒成立；

# x < 1 无解：是因为在(0,1)区间内，guess 只会无限接近 x，而 x**2 < x 恒成立，即 low = guess 恒成立；
