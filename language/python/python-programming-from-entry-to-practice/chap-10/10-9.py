# -*- coding: utf-8 -*-


def show_name(filename):
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()

            print(contents)
    except FileNotFoundError:
        pass


filenames = ['cats.txt', 'dogs.txt']

for file in filenames:
    show_name(file)
