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

# 运算符
print()
print("{0:-^20}".format('运算符'))

print("{0:-^10}".format('左/右移'))
print(2 << 2)
# 10(2) --> 1000(8)
# 8
print(10 << 2)
# 1010(10) --> 101000(40)
# 40
print(11 >> 1)
# 1011(11) --> 101(5)
# 5
print(2 >> 1)
# 10(2) --> 1(1)
# 1

print("{0:-^10}".format('& （按位与）'))
print(5 & 3)
# 101 & 011 = 001
# 1
print(1 & 4)
# 001 & 100 = 000
# 0

print("{0:-^10}".format('| （按位或）'))
print(5 | 3)
# 101 | 011 = 111
# 7
print(1 | 4)
# 001 | 100 = 101
# 5

print("{0:-^10}".format('^ （按位异或）'))
print(5 ^ 3)
# 101 ^ 011 = 110
# 6
print(1 | 4)
# 001 | 100 = 101
# 5

print("{0:-^10}".format('~ （按位取反）'))
print(~5)
# ~5  = -(5+1) = -6
# -6

print()
print("{0:-^20}".format('函数'))

print("{0:-^10}".format('默认参数'))


# 只有形参列表末尾的参数才能指定默认值，
# 即你不能在声明参数列表时先声明有默认值的形参，
# 然后再声明没有默认值的形参。
def default_fn(a, b=5):
    print('a: {} b: {}'.format(a, b))


default_fn(1)
default_fn(2, 3)

print("{0:-^10}".format('关键字参数'))


# 通过为这些参数命名来给赋值
def keyword_fn(a, b=5, c=9):
    print('a: {} b: {} c: {}'.format(a, b, c))


keyword_fn(1, 2)
keyword_fn(1, c=2)
keyword_fn(b=1, a=2)

print("{0:-^10}".format('可变参数'))


# 使用星号 *
# 声明一个带星号的参数 *param 时，
# 从这个参数开始，
# 之后的所有参数都会被收集进入一个名为 param 的元组中。

# 定义了一个带两个星号的参数 **param 时，
# 从这个参数开始，
# 之后的所有参数都会被收入名为 param 的字典中。

def ava_fn(a=1, *num, **phone):
    print('a: ', a)
    for sg_item in num:
        print('num: ', sg_item)

    for f_p, s_p in phone.items():
        print('phone: ', f_p, s_p)


ava_fn(1)
print()
ava_fn(1, 2, 3)
print()
ava_fn(1, 2, 3, jack=111)
print()
ava_fn(1, 2, 3, jack=111, john=222)


# return
def some_fn():
    pass


print(some_fn())

# 文档字符串 ——DocStrings
print()
print("{0:-^20}".format('DocStrings'))


def print_max(x, y):
    '''Prints the maximum of two numbers

    The two values must be integers.'''

    x = int(x)
    y = int(y)

    if x > y:
        print(x, ' is maximum')
    else:
        print(y, ' is maximum')


print_max(3, 5)
print(print_max.__doc__)
