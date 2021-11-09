# -*- coding: utf-8 -*-

import math
import time

# s = 0
# for key in range(11):
#     s += key
# print("result s； ", s)
#
# # e
# num = int(input("Enter a num for e: "))
# res = 1
# fac = 1
# for key in range(1, num):
#     fac *= key
#     res += 1 / fac
#
# print("result e: ", res)

# Π
# while True:
#     fa = 0
#     pi = 0
#     n = int(input("Enter a num for Π: "))
#     for key in range(1, n):
#         fa = (-1) ** (key + 1) * (2 * key - 1)
#         pi += 1 / fa
#     print("result pi: ", 4 * pi)
#     q = input("quit? ")
#     if q == 'y' or q == 'q':
#         break

n = int(input("Enter a num for Π: "))
# 1
fa = 0
pi = 0
fn1_time_start = time.time()
for key in range(1, n):
    fa = (-1) ** (key + 1) * (2 * key - 1)
    pi += 1 / fa
fn1_time_end = time.time()
print("result pi: ", 4 * pi)
print("time cost: ", fn1_time_end - fn1_time_start)

# 2(算法更优化)
pi = 0
sign = 1
divisor = 1
fn2_time_start = time.time()
for i in range(1, n):
    pi += 4 * sign / divisor
    sign *= -1
    divisor += 2
fn2_time_end = time.time()
print("pi is ", pi)
print("time cost: ", fn2_time_end - fn2_time_start)

# 9x9
print("--- 9x9 start ---")
for i in range(1, 10):
    for j in range(1, 10):
        # if i > j:
        #     continue
        print(format(i * j, '3'), end=" ")
    print('')
print("--- 9x9 end ---")
