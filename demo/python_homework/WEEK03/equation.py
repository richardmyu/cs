# -*- coding: utf-8 -*-

import math

# 一元二次方程求解
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c_class: "))

if a != 0:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("No real roots")
    elif delta == 0:
        s = -b / (2 * a)
        print("only one root", s)
    else:
        root = math.sqrt(delta)
        s1 = (-b + root) / (2 * a)
        s2 = (-b - root) / (2 * a)
        print("Has two root, ")
        print("s1: ", s1)
        print("s2: ", s2)
else:
    print("It\'s not a linear equation")
