# -*- coding: utf-8 -*-


def fib(max):
    prev, curr = 0, 1
    while max > 0:
        max -= 1
        yield curr
        prev, curr = curr, prev + curr


if __name__ == '__main__':
    fib = fib(6)

    # 调用 next() 的过程
    for n in fib:
        print(n)

    # raise StopIteration
    print(next(fib))
