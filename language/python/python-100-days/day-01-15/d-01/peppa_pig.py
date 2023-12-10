# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-01-15 22:56:42
Description    : 绘制小猪佩奇
'''
from turtle import *


def nose(x, y):
    """_绘制小猪佩奇-鼻子_

    Args:
        x (_int_): _鼻子起始点 x 坐标_
        y (_int_): _鼻子起始点 y 坐标_
    """
    penup()

    # 将海龟移动到指定的坐标
    goto(x, y)
    pendown()

    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    setheading(-30)
    begin_fill()
    a = 0.4

    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            # 向左转3度
            left(3)
            # 向前走
            forward(a)
        else:
            a = a - 0.08
            left(3)
            forward(a)

    end_fill()
    penup()
    setheading(90)
    forward(25)
    setheading(0)
    forward(10)
    pendown()

    # 设置画笔的颜色(红, 绿, 蓝)
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()
    penup()
    setheading(0)
    forward(20)
    pendown()
    pencolor(255, 155, 192)
    setheading(10)
    begin_fill()
    circle(5)
    color(160, 82, 45)
    end_fill()


def head(x, y):
    """_画头_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    setheading(0)
    pendown()

    begin_fill()
    setheading(180)
    circle(300, -30)
    circle(100, -60)
    circle(80, -100)
    circle(150, -20)
    circle(60, -95)
    setheading(161)
    circle(-300, 15)
    penup()
    goto(-100, 100)
    pendown()
    setheading(-30)
    a = 0.4

    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            lt(3)  # 向左转3度
            fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            lt(3)
            fd(a)

    end_fill()


def ears(x, y):
    """_画耳朵_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    color((255, 155, 192), "pink")
    penup()
    goto(x, y)
    pendown()

    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 54)
    end_fill()

    penup()
    setheading(90)
    forward(-12)
    setheading(0)
    forward(30)
    pendown()

    begin_fill()
    setheading(100)
    circle(-50, 50)
    circle(-10, 120)
    circle(-50, 56)
    end_fill()


def eyes(x, y):
    """_画眼睛_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    color((255, 155, 192), "white")
    penup()
    setheading(90)
    forward(-20)
    setheading(0)
    forward(-95)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()

    color((255, 155, 192), "white")
    penup()
    seth(90)
    forward(-25)
    seth(0)
    forward(40)
    pendown()
    begin_fill()
    circle(15)
    end_fill()

    color("black")
    penup()
    setheading(90)
    forward(12)
    setheading(0)
    forward(-3)
    pendown()
    begin_fill()
    circle(3)
    end_fill()


def cheek(x, y):
    """_画脸颊_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    color((255, 155, 192))
    penup()
    goto(x, y)
    pendown()
    setheading(0)
    begin_fill()
    circle(30)
    end_fill()


def mouth(x, y):
    """_画嘴巴_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    color(239, 69, 19)
    penup()
    goto(x, y)
    pendown()
    setheading(-80)
    circle(30, 40)
    circle(40, 80)


def setting():
    """_设置参数_
    """
    pensize(4)

    # 隐藏海龟
    hideturtle()
    colormode(255)
    color((255, 155, 192), "pink")
    setup(840, 500)
    speed(10)


def main():
    setting()
    nose(-100, 100)
    head(-69, 167)
    ears(0, 160)
    eyes(0, 140)
    cheek(80, 10)
    mouth(-20, 30)
    done()


if __name__ == '__main__':
    main()
