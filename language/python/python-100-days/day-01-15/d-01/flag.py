# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-01-15 22:54:37
Description    : 用 Python 的 turtle 模块绘制国旗
'''
import turtle



def draw_rectangle(x, y, width, height):
    """_绘制矩形_

    Args:
        x (_int_): _矩形起始点 x 坐标_
        y (_int_): _矩形起始点 y 坐标_
        width (_int_): _矩形长度_
        height (_int_): _矩形宽度_
    """
    # 起始点
    turtle.goto(x, y)
    # 画笔颜色
    turtle.pencolor('red')
    # 填充色
    turtle.fillcolor('red')
    # 开始填充
    turtle.begin_fill()

    for i in range(2):
        #
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

    turtle.end_fill()


def draw_star(x, y, radius):
    """_绘制五角星_

    Args:
        x (_int_): _description_
        y (_int_): _description_
        radius (_int_): _description_
    """
    turtle.setpos(x, y)
    pos1 = turtle.pos()
    turtle.circle(-radius, 72)
    pos2 = turtle.pos()
    turtle.circle(-radius, 72)
    pos3 = turtle.pos()
    turtle.circle(-radius, 72)
    pos4 = turtle.pos()
    turtle.circle(-radius, 72)
    pos5 = turtle.pos()
    turtle.color('yellow', 'yellow')
    turtle.begin_fill()
    turtle.goto(pos3)
    turtle.goto(pos1)
    turtle.goto(pos4)
    turtle.goto(pos2)
    turtle.goto(pos5)
    turtle.end_fill()


def main():
    turtle.speed(12)
    turtle.penup()
    x, y = -270, -180

    # 画国旗主体
    width, height = 540, 360
    draw_rectangle(x, y, width, height)

    # 画大星星
    pice = 22
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    turtle.goto(center_x, center_y)
    turtle.left(90)
    turtle.forward(pice * 3)
    turtle.right(90)
    draw_star(turtle.xcor(), turtle.ycor(), pice * 3)
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]

    # 画小星星
    for x_pos, y_pos in zip(x_poses, y_poses):
        turtle.goto(x + x_pos * pice, y + height - y_pos * pice)
        turtle.left(turtle.towards(center_x, center_y) - turtle.heading())
        turtle.forward(pice)
        turtle.right(90)
        draw_star(turtle.xcor(), turtle.ycor(), pice)

    # 隐藏海龟
    turtle.ht()

    # 显示绘图窗口
    turtle.mainloop()


if __name__ == '__main__':
    main()
