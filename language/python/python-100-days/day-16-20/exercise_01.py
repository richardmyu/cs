"""
生成式（推导式）的用法
"""


def main():
    prices = {
        'AAPL': 191.88,
        'GOOG': 1186.96,
        'IBM': 149.24,
        'ORCL': 48.44,
        'ACN': 166.89,
        'FB': 208.09,
        'SYMC': 21.29,
    }

    # 只取值构成列表
    price_list = [value for key, value in prices.items()]
    print(price_list)

    price_list_100 = [value for key, value in prices.items() if value > 100]
    print(price_list_100)

    # 元组列表
    price_list_tuple = [(key, value) for key, value in prices.items()]
    print(price_list_tuple)

    price_list_tuple_100 = [(key, value) for key, value in prices.items() if value > 100]
    print(price_list_tuple_100)

    # 用股票价格大于100元的股票构造一个新的字典
    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)

    test_9_9 = [i * j for i in range(1, 10) for j in range(1, 10)]
    print(test_9_9)

    list_1 = [1, 3, 5, 7, 9]
    list_2 = [1, 2, 4, 6, 8]

    # 交集
    tt_intersect = [i for i in list_1 if i in list_1 and i in list_2]

    # 并集
    tt_union = list_1 + [i for i in list_2 if i not in list_1]

    # 差集
    tt_diff = [i for i in list_1 if i not in list_2]
    print(tt_intersect)
    print(tt_union)
    print(tt_diff)


if __name__ == "__main__":
    main()
