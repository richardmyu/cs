# -*- coding: utf-8 -*-


class Resturant:
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


class IceCreamStand(Resturant):
    def __init__(self, resturant_name, cuisine_type):
        super().__init__(resturant_name, cuisine_type)
        self.flavors = [
            'vanila',
            'chocolate',
            'green tea',
            'strawberry',
            'mongo',
            'lemon',
        ]

    def show_icecream_flavor(self):
        for flavor in self.flavors:
            print(flavor)


tt_icecream = IceCreamStand('tiantian', 'keke')
tt_icecream.show_icecream_flavor()
