"""
迭代工具模块
"""
import itertools

# 产生ABCD的全排列
print('--- ABCD 的全排列 ---')
for i in itertools.permutations('ABCD'):
    print(i)

print()

# 产生ABCDE的五选三组合
print('--- ABCDE 的五选三组合 ---')
for x in itertools.combinations('ABCDE', 3):
    print(x)

print()

# 产生ABCD和123的笛卡尔积
print('--- ABCD 和 123 的笛卡尔积 ---')
for y in itertools.product('ABCD', '123'):
    print(y)

print()

# 产生ABC的无限循环序列
print('--- ABCD 的全排列 ---')
for n in itertools.cycle(('A', 'B', 'C')):
    print(n)
