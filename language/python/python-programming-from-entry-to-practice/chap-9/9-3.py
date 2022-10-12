# -*- coding: utf-8 -*-


class User():

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(f'{self.first_name.title()} {self.last_name.title()}')

    def greet_user(self):
        print(f'Hello, {self.first_name}, have a good day.')


user_1 = User('stuart', 'potter')
user_1.describe_user()
user_1.greet_user()

user_1 = User('bob', 'franklin')
user_1.describe_user()
user_1.greet_user()

user_1 = User('kevin', 'einstein')
user_1.describe_user()
user_1.greet_user()
