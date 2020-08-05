# -*- coding: utf-8 -*-

def p(n):
    x = 1
    i = 1
    while i <= n:
        x *= i
        i += 1
    return x


s1 = p(5)
print("s1 ", s1)
