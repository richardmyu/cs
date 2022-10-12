# -*- coding: utf-8 -*-

guests = ['jack', 'tom', 'marry', 'sophie']
guests[2] = 'rose'

print('I find a big dining-table. I need to invite more friends.')
guests.insert(0, 'King Bob')
guests.insert(int(len(guests) / 2), 'Kevin')
guests.append('Stuart')

print(f'Hi {guests[0]}, welcome to my party!')
print(f'Hi {guests[1]}, welcome to my party!')
print(f'Hi {guests[2]}, welcome to my party!')
print(f'Hi {guests[3]}, welcome to my party!')
print(f'Hi {guests[4]}, welcome to my party!')
print(f'Hi {guests[5]}, welcome to my party!')
print(f'Hi {guests[6]}, welcome to my party!')

# for guest in guests:
#     print(f'Hi {guest}, welcome to my party!')
