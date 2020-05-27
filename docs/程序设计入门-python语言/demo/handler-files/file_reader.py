# -*- coding: utf-8 -*-
filename = 'pi_digits.txt'
"""
open:
    1.读取任何类型文件，首先要打开文件 -- open(filename)
        对应的，使用 close() 关闭文件，但关闭时机问题，不建议使用 close() 来关闭，
        而是使用 with 关键字，让系统自己判断关闭
    2.如果读取文件不在当前目录下，可以使用 相对路径/绝对路径 + 文件名
        Linux/OS X: with open('text_files/filename.txt') as file_object
        windows: with open('text_file\filename.txt') as file_object
        当然，绝对路径更不容易出错

width:
    1.关键字 with，在不需要访问文件后，会关闭（文件）
    2.使用了 width，open 返回的文件对象旧只能在 with 语块中使用
        如果要在外部使用，可以将文件内容储存到列表，在 width 语块外使用这个列表
    
"""

# 全部读取 read()
# with open(filename) as file_object:
#     contents = file_object.read()
#     print("----  start  ----")
#     print(contents.rstrip())
#     print("----  end  ----")

# 逐行读取
# with open(filename) as file_object:
#     # print("----  start  ----")
#     # print(file_object)
#     # print("----  end  ----")
#     # line 每行有两个换行符
#     # 一个是文件中文本本身带有的
#     # 另一个是 print 语句附上的
#     for line in file_object:
#         print(line.rstrip())

# 外部调用
"""
readlines
    从文件读取每一行，并存储在一个列表中
"""
with open(filename) as file_object:
    lines = file_object.readlines()

# for line in lines:
#     print(line.rstrip())

# 使用(读取出来的都是字符串，若需要数值，使用 int()/float())
pi_string = ''
for line in lines:
    pi_string += line.strip()

print("----  start  ----")
print(pi_string)
print("----  end  ----")
print(len(pi_string))

# 检查生日
birthday = input("Enter your birthday,in the form mmddyy: ")
if birthday in pi_string:
    print("yes")
else:
    print("sorry")
