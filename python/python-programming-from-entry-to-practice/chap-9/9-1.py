# -*- coding: utf-8 -*-


class Resturant():

    def __init__(self, resturant_name, cuisine_type):
        self.name = resturant_name
        self.type = cuisine_type

    def describe_resturant(self):
        print(f'resturant name is {self.name}')
        print(f'cuisine type is {self.type}')

    def open_resturant(self):
        print(f'The resturant {self.name} is open')


my_res = Resturant('xiangchuanju', 'wooo')
my_res.describe_resturant()
my_res.open_resturant()
