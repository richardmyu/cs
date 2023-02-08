import time


def func(n):
    for i in range(0, n):
        # yield 相当于 return，
        # 下一次循环从 yield 的下一行开始
        arg = yield i
        print('func', arg)


def test_func():
    f = func(6)

    while True:
        print('main-next:', next(f))
        print('main-send:', f.send(100))
        time.sleep(1)


def test_func_2():
    f = func(6)

    while True:
        print('main-next:', next(f))
        print('main-send:', f.send(None))
        time.sleep(1)


if __name__ == '__main__':
    # test_func()
    test_func_2()
