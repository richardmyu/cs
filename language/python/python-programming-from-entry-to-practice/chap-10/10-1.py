# -*- coding: utf-8 -*-


def first_test():
    with open('pi_digits.txt') as file_object:
        contents = file_object.read()

        print(contents.rstrip())


def second_test():
    with open('pi_digits.txt') as file_object:
        for line in file_object:
            print(line.rstrip())


def third_test():
    pi_str = ''

    with open('pi_digits.txt') as file_object:
        lines = file_object.readlines()

    for line in lines:
        pi_str += line.strip()

    print(pi_str)


first_test()
second_test()
third_test()
