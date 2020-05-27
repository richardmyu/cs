# -*- coding: utf-8 -*-

# ZeroDivisionError: division by zero
# print(5/0)

try:
    print(5 / 0)
except ZeroDivisionError:
    print("you can't divide by zero!")

print("Give me two numbers, and i'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num == 'q':
        break
    second_num = input("\nSecond number: ")
    if second_num == 'q':
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("\nYou can't divide by zero!")
    else:
        print(answer)

# 文件异常
# 读取不存在的文件，异常:
# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
filename = 'alice.txt'
# with open(filename) as file_object:
#     contents = file_object.read()

try:
    with open(filename) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    print("\nSorry, the file " + filename + " does not exist.")
