import json


def main():
    mydict = {
        'name': 'bob',
        'age': 5,
        'friends': ['kevin', 'stewart'],
        'cars': [
            {'brand': 'Hearts', 'count': 320},
            {'brand': 'Diamonds', 'count': 320},
            {'brand': 'Clubs', 'count': 320},
            {'brand': 'Spades', 'count': 320},
        ],
    }

    try:
        with open('data.json', 'w', encoding='utf-8') as fs:
            json.dump(mydict, fs)
    except IOError as e:
        print(e)
    print('保存数据完成!')


if __name__ == '__main__':
    main()
