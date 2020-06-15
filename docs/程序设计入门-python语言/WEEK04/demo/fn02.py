# -*- coding: utf-8 -*-

x = 1


def fn1():
    x = 2
    print(x)


fn1()
print(x)

y = 12


def fn2():
    global y
    y = 21
    print(y)


fn2()
print(y)
