# -*- coding: utf-8 -*-

import time

milion_list = list(range(1, 1000001))

print(f'min number is {min(milion_list)}')
print(f'max number is {max(milion_list)}')

strat_time = time.time()
print(f'sum number is {sum(milion_list)}')

end_time = time.time()
print(f'sum time is {end_time-strat_time}')
