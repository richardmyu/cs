'''双色球选号
红球号码范围为 01-33
蓝球号码范围为 01-16
双色球每期从 33 个红球中开出 6 个号码
从 16 个蓝球中开出 1 个号码作为中奖号码
开奖号码的 6 个红球号码和 1 个蓝球号码，顺序不限
'''

from random import randint, sample


def display(balls):
    '''
    输出列表中的双色球号码
    '''
    for index, ball in enumerate(balls):
        if index == len(balls) - 1:
            print('|', end=' ')
        print('%02d' % ball, end=' ')
    print()


def random_select():
    '''
    随机选择一组号码
    '''
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))
    return selected_balls


def main():
    n = int(input('机选几注: '))
    for _ in range(n):
        display(random_select())


if __name__ == '__main__':
    main()
