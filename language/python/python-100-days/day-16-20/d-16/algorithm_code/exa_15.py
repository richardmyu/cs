"""
迭代器 - __iter__ / __next__
itertools - 生成可迭代序列的工具模块
"""

from math import sqrt


def is_prime(num):
    for factor in range(2, int(sqrt(num)) + 1):
        if num % factor == 0:
            return False

    return True


class PrimeIter(object):
    def __init__(self, min_value, max_value):
        assert 2 <= min_value <= max_value
        self.min_value = min_value
        self.max_value = max_value

    def __iter__(self):
        return self

    def __next__(self):
        self.min_value += 1

        while self.min_value <= self.max_value:
            if is_prime(self.min_value):
                return self.min_value

            self.min_value += 1

        raise StopIteration()


class FibIter(object):
    def __ini__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1

            return self.a

        raise StopIteration()


def main():
    prime_iter = PrimeIter(2, 1000)

    for val in prime_iter:
        print(val)


if __name__ == '__main__':
    main()