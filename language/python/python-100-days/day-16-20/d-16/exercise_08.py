"""穷举法
又称为暴力破解法，对所有的可能性进行验证，直到找到正确答案。

例子：百钱百鸡和五人分鱼。
"""


def buy_chickens():
    '''
    公鸡 5 元一只
    母鸡 3 元一只
    小鸡 1 元三只
    用 100 元买 100 只鸡
    问公鸡/母鸡/小鸡各多少只
    '''
    for x in range(20):
        for y in range(33):
            z = 100 - x - y
            if 5 * x + 3 * y + z // 3 == 100 and z % 3 == 0:
                print(x, y, z)


def distribute_fish():
    '''
    A、B、C、D、E 五人在某天夜里合伙捕鱼
    最后疲惫不堪各自睡觉
    第二天 A 第一个醒来，他将鱼分为 5 份，扔掉多余的 1 条，拿走自己的一份
    B 第二个醒来，也将鱼分为 5 份，扔掉多余的 1 条，拿走自己的一份
    然后 C、D、E 依次醒来也按同样的方式分鱼
    问他们至少捕了多少条鱼
    '''
    fish = 6
    while True:
        total = fish
        enough = True
        for _ in range(5):
            if (total - 1) % 5 == 0:
                total = (total - 1) // 5 * 4
            else:
                enough = False
                break
        if enough:
            print(fish)
            break
        fish += 5


if __name__ == '__main__':
    buy_chickens()
    distribute_fish()
