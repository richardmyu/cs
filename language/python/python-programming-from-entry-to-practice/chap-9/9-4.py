# -*- coding: utf-8 -*-


class Resturant():

    def __init__(self, resturant_name, cuisine_type):
        self.name = resturant_name
        self.type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        print(f'resturant name is {self.name}')
        print(f'cuisine type is {self.type}')

    def open_resturant(self):
        print(f'The resturant {self.name} is open')

    def set_number_served(self, num):
        if num < 0:
            return
        self.number_served = num

    def increment_number_served(self, num):
        if num < 0:
            return
        self.number_served = self.number_served + num


my_res = Resturant('xiangchuanju', 'wooo')
print(my_res.number_served)
my_res.set_number_served(20)
print(my_res.number_served)
my_res.increment_number_served(120)
print(my_res.number_served)
