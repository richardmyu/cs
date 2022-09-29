# -*- coding: utf-8 -*-

from resturant import Resturant

my_res = Resturant('chongqinxiaomian', 'wowww')

print(my_res.number_served)
my_res.set_number_served(20)
print(my_res.number_served)
my_res.increment_number_served(120)
print(my_res.number_served)
