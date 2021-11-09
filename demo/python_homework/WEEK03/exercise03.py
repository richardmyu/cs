# -*- coding: utf-8 -*-

import math

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
