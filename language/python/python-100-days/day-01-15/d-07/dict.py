def fn_1():
    # 创建字典的字面量语法
    scores = {'kevin': 8, 'bob': 2, 'sturat': 5}
    print(scores)

    # 创建字典的构造器语法
    items1 = dict(one=1, two=2, three=3, four=4)

    # 通过zip函数将两个序列压成字典
    items2 = dict(zip(['a', 'b', 'c'], '123'))

    # 创建字典的推导式语法
    items3 = {num: num**2 for num in range(1, 10)}
    print(items1, items2, items3)

    # 通过键可以获取字典中对应的值
    print(scores['kevin'])
    print(scores['sturat'])

    # 对字典中所有键值对进行遍历
    for key in scores:
        print(f'{key}: {scores[key]}')

    # 更新字典中的元素
    scores['kevin'] = 9
    scores['bob'] = 7
    scores.update(doraemon=9, nobita=8)
    print(scores)

    if 'shizuka' in scores:
        print(scores['shizuka'])

    print(scores.get('shizuka'))

    # get方法也是通过键获取对应的值但是可以设置默认值
    print(scores.get('shizuka', 8))

    # 删除字典中的元素
    print(scores.popitem())
    print(scores.popitem())
    print(scores.pop('shizuka', 8))

    # 清空字典
    scores.clear()
    print(scores)


if __name__ == '__main__':
    fn_1()
