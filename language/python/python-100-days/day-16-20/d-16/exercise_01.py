'''生成式（推导式）的用法'''


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

    price_list = [value for key, value in prices.items()]
    print(price_list)

    price_list_tuple = [(key, value) for key, value in prices.items()]
    print(price_list_tuple)

    # 用股票价格大于100元的股票构造一个新的字典
    prices2 = {key: value for key, value in prices.items() if value > 100}
    print(prices2)


if __name__ == "__main__":
    main()
