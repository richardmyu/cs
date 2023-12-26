# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-02-11 20:56:08
Description    : 约瑟夫环问题
    《幸运的基督徒》
    有15个基督徒和15个非基督徒在海上遇险
    为了能让一部分人活下来不得不将其中15个人扔到海里面去
    有个人想了个办法就是大家围成一个圈
    由某个人开始从 1 报数
    报到 9 的人就扔到海里面
    他后面的人接着从 1 开始报数
    报到 9 的人继续扔到海里面
    直到扔掉 15 个人
    由于上帝的保佑
    15 个基督徒都幸免于难
    问这些人最开始是怎么站的
    哪些位置是基督徒哪些位置是非基督徒。
'''
def main():
    # 总人数
    persons = [True] * 30
    counter, index, number = 0, 0, 0

    while counter < 15:
        if persons[index]:
            number += 1

            if number == 9:
                persons[index] = False
                counter += 1
                number = 0

        index += 1
        index %= 30

    for person in persons:
        print('基' if person else '非', end='')


if __name__ == '__main__':
    main()
