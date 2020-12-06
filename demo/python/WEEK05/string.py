# -*- coding: utf-8 -*-

strSingle = 'hi\' hello\nworld!\nhhh'

strQuote = "hi\' hello\nworld!\nhhh"

strTriple = """hi\'
 hello\n

 world!\nhhh
 """

print("-----------------------")
print(strSingle)
print("-----------------------")
print(strQuote)
print("-----------------------")
print(strTriple)
print("-----------------------")

# len
print(len("hello"))
print(len("hello\n"))

# +
print("hello" + " " + "world" + "!")

# *
print("呱"*3)
print("哈"*3)

# in
print("he" in "hello world")
print("wo" in "hello world")
print("we" in "hello world")
print("Wo" in "hello world")

# for
for s in "hellow":
    print(s)


# index
indStr = "hello world"

# print(indStr[0], indStr[0-len(indStr)])
# print(indStr[1])
# print(indStr[-1])

# print(indStr[11])

# slicing

# print(indStr[0:])
# print(indStr[:4])
# print(indStr[2:4])
# print(indStr[2:8])
# print(indStr[2:8:2])

# print(indStr[::1])
# print(indStr[::-1])
# print(indStr[::-2])

# indStr[2] = 'a'

# replace
# indStr = indStr.replace("e", "a")
# print(indStr)

# indStr = indStr.replace("l", "-")
# print(indStr)

# find
# print(indStr.find("hello"))
# print(indStr.find("hall"))
# print(indStr.find(" "))

# split

print(indStr.split())
# print(indStr.split(" "))
# print(indStr.split("o"))

print('a' > 'b')
print('abc' > 'a c')

# format

print("hello {}, today is {}".format("张三", "2020-12-06"))
