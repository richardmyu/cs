# -*- coding: utf-8 -*-

n = int(input("Enter one number: "))
if n < 0:
    print("please enter a positive ")
else:
    while n != 1:
        print(int(n))
        if n % 2 != 0:
            n = 3 * n + 1
        else:
            n /= 2

print("result ", int(n))
