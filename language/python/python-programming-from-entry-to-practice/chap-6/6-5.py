river_country = {
    'changjiang': 'china',
    'huanghe': 'china',
    'jinghangdayunhe': 'china',
}

for key, val in river_country.items():
    print(f'{key} is in {val}')

for key, val in sorted(river_country.items()):
    print(f'{key} is in {val}')

for val in river_country.keys():
    print(val)

for val in river_country.values():
    print(val)
