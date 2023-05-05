"""
迭代工具模块
"""
import itertools

# 产生 ABCD 的全排列
print('--- ABCD 的全排列 ---')
for i in itertools.permutations('ABCD'):
    print(i)

print()

# 产生 ABCDE 的五选三组合
print('--- ABCDE 的五选三组合 ---')
for x in itertools.combinations('ABCDE', 3):
    print(x)

print()

# 产生 ABCD 和 123 的笛卡尔积
print('--- ABCD 和 123 的笛卡尔积 ---')
for y in itertools.product('ABCD', '123'):
    print(y)

for c in itertools.product('♥♠♣♦','23456789JQKA'):
    print(c)

for cc in itertools.combinations(itertools.product('♥♠♣♦','JQKA'),16):
    print(cc)

print()

# 产生 ABC 的无限循环序列
print('--- ABCD 的全排列 ---')
# for n in itertools.cycle(('A', 'B', 'C')):
#     print(n)
