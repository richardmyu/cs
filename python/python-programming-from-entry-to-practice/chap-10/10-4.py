# -*- coding: utf-8 -*-

while True:
    name = input('\nPlease enter your name(enter q to quit): ')
    if name != 'q':
        print(f'Hello {name}')
        with open('guest_book.txt', 'a') as file_object:
            file_object.write(name + '\n')
    else:
        break
