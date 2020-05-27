# -*- coding: utf-8 -*-
import json

# username = input("What is your name? ")

# filename = "data/username.json"

# with open(filename, 'w') as f_obj:
#     json.dump(username, f_obj)
#     print("We'll remember you when you com back, " + username + "!")

# def greet_user():
#     filename = 'data/username.json'
#     try:
#         with open(filename) as f_obj:
#             username = json.load(f_obj)
#     except FileNotFoundError:
#         username = input("What is your name? ")
#         with open(filename, 'w') as f_obj:
#             json.dump(username, f_obj)
#             print("We'll remember you when you com back, " + username + "!")
#     else:
#         print("Welcome back, " + username + "!")
#
# greet_user()

# 重构
filename = 'data/username.json'


def get_stored_username():
    try:
        with open(filename, 'r', encoding='utf-8') as f_obj:
            try:
                username = json.load(f_obj)
            except json.decoder.JSONDecodeError:
                username = ''
            # f_obj.read() and json.load(f_obj)
            # # 只有第一次有效访问???
            # contents = f_obj.read()
            # print(contents)
            # print(f_obj)
            # if len(contents) > 0:
            #     username = json.load(f_obj)
            # else:
            #     username = ''
    except FileNotFoundError:
        return None
    else:
        return username


def get_new_username():
    username = input("What is your name? ")
    with open(filename, 'w', encoding='utf-8') as f_obj:
        json.dump(username, f_obj)
    return username


def greet_user():
    username = get_stored_username()
    if username:
        print("Welcome back, " + username + "!")
    else:
        username = get_new_username()
        print("We'll remember you when you com back, " + username + "!")


greet_user()
