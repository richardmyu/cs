# -*- coding: utf-8 -*-

# 写入文件
filename = 'programming.txt'
"""
open()
    第二个参数：
        'r' - 表示 读取模式（默认）
        'w' - 表示 写入模式
        'a' - 表示 附加模式(即不会覆盖原来的数据，而是添加新数据)
        'r+' - 表示 读取和写入模式
        
write()
    1.将字符写入文件（非字符，必须使用 str() 转化）
    2.不会在写入的文本末尾添加换行符，需手动添加 \n
"""
with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love music.\n")
    file_object.write("I love book.\n")
    file_object.write("Just a joke.\n")

# 覆盖上次写入的数据
# with open(filename, 'w') as file_object:
#     file_object.write("I don't love programming.\n")
#     file_object.write("I don't love music.\n")
#     file_object.write("I don't love book.\n")
#     file_object.write("Not a joke.\n")

# 不会覆盖上次写入的数据
with open(filename, 'a') as file_object:
    file_object.write("I don't love programming.\n")
    file_object.write("I don't love music.\n")
    file_object.write("I don't love book.\n")
    file_object.write("Not a joke.\n")

# demo
quit_text = ''
while True:
    quit_text = str(input("Enter the reason for you programming? "))
    if quit_text.lower() == 'q':
        break
    with open(filename, 'a') as file_object:
        file_object.write(quit_text + "\n")
