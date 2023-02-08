import math


def excecise_1():
    '''英制单位英寸和公制单位厘米互换'''
    value = float(input('请输入长度(0-100): '))
    unit = input('请输入单位(in, cm): ')

    if unit == 'in':
        print(f'{ value } 英寸 = { value * 2.54 } 厘米')
    elif unit == 'cm':
        print(f'{ value } 厘米 = { value / 2.54 } 英寸')
    else:
        print('请输入有效的数值或限定的单位')


def excecise_2():
    '''百分制成绩转换为等级制成绩'''
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
    '''输入三条边长，如果能构成三角形就计算周长和面积'''
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
    excecise_1()
    excecise_2()
    excecise_3()
