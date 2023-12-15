# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-01-15 22:56:42
Description    : 绘制小猪佩奇
'''
import turtle as tt


def pig_nose(x, y):
    """_绘制小猪佩奇-鼻子_

    Args:
        x (_int_): _鼻子起始点 x 坐标_
        y (_int_): _鼻子起始点 y 坐标_
    """
    tt.penup()

    # 将海龟移动到指定的坐标
    tt.goto(x, y)
    tt.pendown()

    # 设置海龟的方向（0-东、90-北、180-西、270-南）
    tt.setheading(-30)
    tt.begin_fill()
    a = 0.4

    for i in range(120):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            # 向左转3度
            tt.left(3)
            # 向前走
            tt.forward(a)
        else:
            a = a - 0.08
            tt.left(3)
            tt.forward(a)

    tt.end_fill()
    tt.penup()
    tt.setheading(90)
    tt.forward(25)
    tt.setheading(0)
    tt.forward(10)
    tt.pendown()

    # 设置画笔的颜色(红, 绿, 蓝)
    tt.pencolor(255, 155, 192)
    tt.setheading(10)
    tt.begin_fill()
    tt.circle(5)
    tt.color(160, 82, 45)
    tt.end_fill()
    tt.penup()
    tt.setheading(0)
    tt.forward(20)
    tt.pendown()
    tt.pencolor(255, 155, 192)
    tt.setheading(10)
    tt.begin_fill()
    tt.circle(5)
    tt.color(160, 82, 45)
    tt.end_fill()


def pig_head(x, y):
    """_画头_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    tt.color((255, 155, 192), "pink")
    tt.penup()
    tt.goto(x, y)
    tt.setheading(0)
    tt.pendown()

    tt.begin_fill()
    tt.setheading(180)
    tt.circle(300, -30)
    tt.circle(100, -60)
    tt.circle(80, -100)
    tt.circle(150, -20)
    tt.circle(60, -95)
    tt.setheading(161)
    tt.circle(-300, 15)
    tt.penup()
    tt.goto(-100, 100)
    tt.pendown()
    tt.setheading(-30)
    a = 0.4

    for i in range(60):
        if 0 <= i < 30 or 60 <= i < 90:
            a = a + 0.08
            tt.lt(3)  # 向左转3度
            tt.fd(a)  # 向前走a的步长
        else:
            a = a - 0.08
            tt.lt(3)
            tt.fd(a)

    tt.end_fill()


def pig_ears(x, y):
    """_画耳朵_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    tt.color((255, 155, 192), "pink")
    tt.penup()
    tt.goto(x, y)
    tt.pendown()

    tt.begin_fill()
    tt.setheading(100)
    tt.circle(-50, 50)
    tt.circle(-10, 120)
    tt.circle(-50, 54)
    tt.end_fill()

    tt.penup()
    tt.setheading(90)
    tt.forward(-12)
    tt.setheading(0)
    tt.forward(30)
    tt.pendown()

    tt.begin_fill()
    tt.setheading(100)
    tt.circle(-50, 50)
    tt.circle(-10, 120)
    tt.circle(-50, 56)
    tt.end_fill()


def pig_eyes(x, y):
    """_画眼睛_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    tt.color((255, 155, 192), "white")
    tt.penup()
    tt.setheading(90)
    tt.forward(-20)
    tt.setheading(0)
    tt.forward(-95)
    tt.pendown()
    tt.begin_fill()
    tt.circle(15)
    tt.end_fill()

    tt.color("black")
    tt.penup()
    tt.setheading(90)
    tt.forward(12)
    tt.setheading(0)
    tt.forward(-3)
    tt.pendown()
    tt.begin_fill()
    tt.circle(3)
    tt.end_fill()

    tt.color((255, 155, 192), "white")
    tt.penup()
    tt.seth(90)
    tt.forward(-25)
    tt.seth(0)
    tt.forward(40)
    tt.pendown()
    tt.begin_fill()
    tt.circle(15)
    tt.end_fill()

    tt.color("black")
    tt.penup()
    tt.setheading(90)
    tt.forward(12)
    tt.setheading(0)
    tt.forward(-3)
    tt.pendown()
    tt.begin_fill()
    tt.circle(3)
    tt.end_fill()


def pig_cheek(x, y):
    """_画脸颊_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    tt.color((255, 155, 192))
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.setheading(0)
    tt.begin_fill()
    tt.circle(30)
    tt.end_fill()


def pig_mouth(x, y):
    """_画嘴巴_

    Args:
        x (_type_): _description_
        y (_type_): _description_
    """
    tt.color(239, 69, 19)
    tt.penup()
    tt.goto(x, y)
    tt.pendown()
    tt.setheading(-80)
    tt.circle(30, 40)
    tt.circle(40, 80)


def pig_setting():
    """_设置参数_
    """
    tt.pensize(4)

    # 隐藏海龟
    tt.hideturtle()
    tt.colormode(255)
    tt.color((255, 155, 192), "pink")
    tt.setup(840, 500)
    tt.speed(10)


def main():
    pig_setting()
    pig_nose(-100, 100)
    pig_head(-69, 167)
    pig_ears(0, 160)
    pig_eyes(0, 140)
    pig_cheek(80, 10)
    pig_mouth(-20, 30)
    tt.done()


if __name__ == '__main__':
    main()
