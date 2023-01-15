# -*- coding: utf-8 -*-

favorite_place = {
    'bob': ['beijing', 'tainjing', 'daliang'],
    'kevin': ['chongqing'],
    'stuart': ['shanghai', 'guangzhou', 'hangzhou', 'nanjing'],
}

for name, places in favorite_place.items():
    if len(places) > 1:
        print(f'{name} like places are {places}')
    else:
        print(f'{name} favorite place is {places}')
