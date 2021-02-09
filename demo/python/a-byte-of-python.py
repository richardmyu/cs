# -*- coding: utf-8 -*-

# print 总是以一个不可见的 「新的一行」 字符（\n）作为结尾
print("Hello ", end='')
print("World!", end=' ')
print("Welcome", end=' ')
print("new world!")

# format
print()
print("{0:-^20}".format('format'))
age = 20
name = '张三'
print('{0} was {1}'.format(name, age))
# 等价
print(name + ' was ' + str(age))

# 数字非必填（自动填充）
print('{} was {}'.format(name, age))

# 取十进制小数点后的精度为 3 ，得到的浮点数为 '0.333'
print('{0:.3f}'.format(1.0 / 3))

# 填充下划线 (_) ，文本居中
# 将 '___hello___' 的宽度扩充为 11
print('{0:_^11}'.format('hello'))

# 用基于关键字的方法打印显示
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

# 转义序列
print()
print("{0:-^20}".format('转义序列'))
# 引号混乱
print('he\'s a good man')
print("he's a good man")
# \\ 转义 \
print("he's a good \\n man")
# 多行文本
#     1.\n
#     2.''' xx ''' 三引号
print('''
Hi!
Good boy.
''')

# 行末尾的单个反斜杠表示字符串在下一行中继续，但不添加换行符
print("This is the first sentence.\
This is the second sentence.")

# 原始字符串
# 指定一些没有特殊处理（转义序列等）的字符串
# 在字符串前面加上 r 或者 R
# 在处理正则表达式时，我们一般使用原始字符串。
# 否则，可能需要进行大量的反向操作
print(r"Newlines are indicated by \n")

