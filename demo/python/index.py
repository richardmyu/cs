# -*- coding: utf-8 -*-

import random

goal_num = random.randint(1, 10)
is_loop = True

print("Guess what I think (1-10)")


def guess_num():
    n = int(input('number is: '))
    if n < goal_num:
        print('your answer is too small.')
    elif n > goal_num:
        print('your answer is too large.')
    else:
        global is_loop
        is_loop = False
        print('BINGO!')


while is_loop:
    guess_num()
