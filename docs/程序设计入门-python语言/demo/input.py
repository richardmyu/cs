# -*- coding: utf-8 -*-

msg = "Tell me something, and i will repeat it back to you."
msg += "\nHow do you think read book： "
if input(msg).lower() == 'it is good':
    print("you are great")
else:
    print("maybe you can try")

print(int(input("how old are you? ")))

num = input("enter a num, i will tell you if it's even or odd: ")
num = int(num)
if num % 2 == 0:
    print("\nThe num " + str(num) + ' is even')
else:
    print("\nThe num " + str(num) + ' is odd')
