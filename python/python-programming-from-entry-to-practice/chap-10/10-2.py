# -*- coding: utf-8 -*-

with open('pi_digits.txt') as file_object:
    for line in file_object:
        print(line.rstrip().replace('2', '*'))
