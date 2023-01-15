# -*- coding: utf-8 -*-

cities = {
    'beijing': {'couuntry': 'china', 'population': '2173', 'fact': 'capital'},
    'shanghai': {'couuntry': 'china', 'population': '2420', 'fact': 'economic center'},
    'guangzhou': {'couuntry': 'china', 'population': '1404', 'fact': 'trade cente'},
}

cities['shengzhen'] = {
    'couuntry': 'china',
    'population': '1191',
    'fact': 'special economic zone',
}

for city, obj in cities.items():
    for key, val in obj.items():
        print(f'{city.title()} -- {key.title()} : {val}')
