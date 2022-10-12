# -*- coding: utf-8 -*-

harry = {
    'first_name': 'harry',
    'last_name': 'potter',
    'age': 18,
    'city': 'london'
}

hermione = {
    'first_name': 'hermione',
    'last_name': 'granger',
    'age': 19,
    'city': 'london'
}

ronald = {
    'first_name': 'rronald',
    'last_name': 'weasley',
    'age': 18,
    'city': 'london'
}

people = [harry, hermione, ronald]

for person in people:
    for name, val in person.items():
        print(f'{person["first_name"]} {name} is {val}')
