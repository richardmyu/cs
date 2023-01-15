# -*- coding: utf-8 -*-

name = "\nWhat is your name? "
place = "\nIf you could visit one place in the world, where would you go? "

while True:
    msg_name = input(name)
    msg_place = input(place)

    if msg_name != 'quit' and msg_place != 'quit':
        print(f'{msg_name} want to {msg_place}')
    else:
        break
