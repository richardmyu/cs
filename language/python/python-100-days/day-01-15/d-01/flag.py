# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-01-15 22:54:37
Description    : 用 Python 的 turtle 模块绘制国旗
'''
import turtle as tt


def draw_rectangle(x, y, width, height):
    """_绘制矩形_

    Args:
        x (_int_): _矩形起始点 x 坐标_
        y (_int_): _矩形起始点 y 坐标_
        width (_int_): _矩形长度_
        height (_int_): _矩形宽度_
    """
    # 起始点
    tt.goto(x, y)

    # 画笔颜色
    tt.pencolor('red')

    # 填充色
    tt.fillcolor('red')

    # 开始填充
    tt.begin_fill()

    for i in range(2):
        #
        tt.forward(width)
        tt.left(90)
        tt.forward(height)
        tt.left(90)

    tt.end_fill()


def draw_star(x, y, radius):
    """_绘制五角星_

    Args:
        x (_int_): _description_
        y (_int_): _description_
        radius (_int_): _description_
    """
    tt.setpos(x, y)
    pos1 = tt.pos()
    tt.circle(-radius, 72)
    pos2 = tt.pos()
    tt.circle(-radius, 72)
    pos3 = tt.pos()
    tt.circle(-radius, 72)
    pos4 = tt.pos()
    tt.circle(-radius, 72)
    pos5 = tt.pos()

    tt.color('yellow', 'yellow')
    tt.begin_fill()
    tt.goto(pos3)
    tt.goto(pos1)
    tt.goto(pos4)
    tt.goto(pos2)
    tt.goto(pos5)
    tt.end_fill()


def main():
    tt.speed(12)
    tt.penup()
    x, y = -270, -180

    # 画国旗主体
    width, height = 540, 360
    draw_rectangle(x, y, width, height)

    # 画大星星
    pice = 22
    center_x, center_y = x + 5 * pice, y + height - pice * 5
    tt.goto(center_x, center_y)
    tt.left(90)
    tt.forward(pice * 3)
    tt.right(90)
    draw_star(tt.xcor(), tt.ycor(), pice * 3)
    x_poses, y_poses = [10, 12, 12, 10], [2, 4, 7, 9]

    # 画小星星
    for x_pos, y_pos in zip(x_poses, y_poses):
        tt.goto(x + x_pos * pice, y + height - y_pos * pice)
        tt.left(tt.towards(center_x, center_y) - tt.heading())
        tt.forward(pice)
        tt.right(90)
        draw_star(tt.xcor(), tt.ycor(), pice)

    # 隐藏海龟
    tt.ht()

    # 显示绘图窗口
    tt.mainloop()


if __name__ == '__main__':
    main()
