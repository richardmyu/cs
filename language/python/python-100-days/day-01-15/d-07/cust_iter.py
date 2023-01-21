# -*- coding: utf-8 -*-


class Fib(object):
    def __init__(self, max=0):
        super(Fib, self).__init__()
        self.prev = 0
        self.curr = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.max > 0:
            self.max -= 1
            # 当前要返回的元素的值
            value = self.curr
            # 下一个要返回的元素的值
            self.curr += self.prev
            # 设置下一个元素的上一个元素的值
            self.prev = value
            return value
        else:
            raise StopIteration

    # 兼容Python2.x
    def next(self):
        return self.__next__()


if __name__ == '__main__':
    fib = Fib(10)
    # 调用next()的过程
    for n in fib:
        print(n)
    # raise StopIteration
    print(next(fib))
