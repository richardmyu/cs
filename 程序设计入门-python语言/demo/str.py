# -*- coding: utf-8 -*-

# 空格符
# \t 制表符
# \n 换行符
# \ 转义符
print("\thello")
print("world\n")
print("\thello\n\tworld")
print('he\'s book')

# 字符串拼接
first_name = "jack"
last_name = "lovelace"
full_name = first_name + " " + last_name

print(full_name)

# title() : 字符首字母大写
print(full_name.title())

# strip/rstrip/lstrip 去除空格
message = " hello world "
print("[" + message.rstrip() + "]")
print("[" + message.lstrip() + "]")
print("[" + message.strip() + "]")


