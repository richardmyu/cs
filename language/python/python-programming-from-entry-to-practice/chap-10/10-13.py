# -*- coding: utf-8 -*-

from cgi import print_arguments
import json
filename = 'username.json'

def get_stored_username():
    try:
        global filename
        with open(filename) as f_obj:
            username=json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    username=input("what\'s your name? ")
    global filename
    with open(filename,'w') as b_obj:
        json.dump(username,b_obj)
    return username

def greet_user():
    username=get_stored_username()
    if username:
        is_name = input(f"Is you {username} (enter yes/no)?")
        if is_name=='yes':
            print(f'Welcome back, {username}!')
        else:
            username = get_new_username()
            print(f'We\'ll remember you when you come back, {username}!')
    else:
        username=get_new_username()
        print(f'We\'ll remember you when you come back, {username}!')

greet_user()
