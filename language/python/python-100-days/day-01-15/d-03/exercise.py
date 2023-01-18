# -*- coding: utf-8 -*-

import math


def fn_1():
    username = input('请输入用户名: ')
    password = input('请输入口令: ')

    if username == 'admin' and password == '123456':
        print('身份验证成功!')
    else:
        print('身份验证失败!')


def fn_2():
    x = float(input('x = '))

    if x > 1:
        y = 3 * x - 5
    elif x >= -1:
        y = x + 2
    else:
        y = 5 * x + 3
    print('f(%.2f) = %.2f' % (x, y))


def fn_2_2():
    x = float(input('x = '))

    if x > 1:
        y = 3 * x - 5
    else:
        if x >= -1:
            y = x + 2
        else:
            y = 5 * x + 3
    print('f(%.2f) = %.2f' % (x, y))


def excecise_1():
    """英制单位英寸和公制单位厘米互换"""
    value = float(input('请输入长度(0-100): '))
    unit = input('请输入单位(in, cm): ')

    if unit == 'in':
        print(f'{ value } 英寸 = { value * 2.54 } 厘米')
    elif unit == 'cm':
        print(f'{ value } 厘米 = { value / 2.54 } 英寸')
    else:
        print('请输入有效的数值或限定的单位')


def excecise_2():
    """百分制成绩转换为等级制成绩"""
    score = float(input('请输入成绩(0-100): '))

    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'E'

    print(f'百分制成绩 {score} 对应的等级是：{ grade }')


def excecise_3():
    """输入三条边长，如果能构成三角形就计算周长和面积"""
    a = float(input('a = '))
    b = float(input('b = '))
    c = float(input('c = '))

    if a + b > c and a + c > b and b + c > a:
        print(f'三角形周长: { a + b + c }')
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print(f'三角形面积: { area }')
    else:
        print('不能构成三角形')


if __name__ == '__main__':
    fn_1()
    fn_2()
    excecise_1()
    excecise_2()
    excecise_3()
