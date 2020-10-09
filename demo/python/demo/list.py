# -*- coding: utf-8 -*-

# 创建列表
names = ["张三", "李四", "小黄人", "大眼", "妖狐"]

# 读取列表
# print(names[0])
# print(names[-1])

# 修改
names[1] = "孙悟空"
# print(names[1])

# 添加
names.append("苏苏呀")
# print(names)

# 插入
names.insert(1, "李四")
# print(names)

# 删除 -- del
# del names[1]
# print(names)

# 删除 -- remove
# 不带索引，默认删除最后一个
# names.pop()
# print(names)
# 带索引，删除指定
# names.pop(1)
# print(names)
# names.pop(9)
# 不存在的索引值，会报错：pop index out of range

# 删除 -- remove
# 删除不存在的值，会报错：list.remove(x): x not in list
# names.remove("王五")
# names.remove("小黄人")

# 排序
# sort() 改变原列表
# names.sort()
# print("sort-- ", names)

letters = ['a', 'b', 'ab', 'ac', 'AA', 'B', 'A']
# letters.sort()
# print("sort-- ", letters)

# 逆序code1
# letters.sort(reverse=True)
# print("sort(reverse)-- ", letters)

# sorted 不改变原列表
# print("sorted-- ", sorted(letters))
# print("sorted(reverse)-- ", sorted(letters, reverse=True))
# print(letters)

# 反转列表 reverse
# letters.reverse()
# print("reverse-- ", letters)

# 列表长度
# print(len(letters))

# for
for item in letters:
    print(item)

# 外部访问到的是最后一次循环的结果
print("out ", item)

# 创建数值列表
print(range(1, 5))
for num in range(1, 5):
    print("num is ", num)

for even_num in range(0, 11, 2):
    print("even num ", even_num)

# list() 转换成列表
print(list(range(1, 5)))

nums = list(range(1, 11))
print(min(nums))
print(max(nums))
print(sum(nums))

# 列表解析
vals = []
for val in range(1, 11):
    vals.append(val ** 2)
print(vals)

squares = [value ** 2 for value in range(1, 11)]
print(squares)

# 切片
persons = ["张三", "李四", "小明", "小红", "jack", "tom"]
print(persons[0:2])
print(persons[2:])
print(persons[:4])
print(persons[-2:])
# 遍历切片
for person in persons[:4]:
    print('person ', person)

# 复制列表
print(persons[:])

# 不可变的列表-->元组
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[-1])
# IndexError: tuple index out of range
# print(dimensions[9])

# TypeError: 'tuple' object does not support item assignment
# dimensions[0] = 100

for dim in dimensions:
    print('dim ', dim)

