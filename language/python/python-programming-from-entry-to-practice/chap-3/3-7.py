guests = ['jack', 'tom', 'marry', 'sophie']
guests[2] = 'rose'

guests.insert(0, 'King Bob')
guests.insert(int(len(guests) / 2), 'Kevin')
guests.append('Stuart')

print('only two guests...')
print(f'sorry {guests.pop()}, i could not invite you to my party.')
print(f'sorry {guests.pop()}, i could not invite you to my party.')
print(f'sorry {guests.pop()}, i could not invite you to my party.')
print(f'sorry {guests.pop()}, i could not invite you to my party.')
print(f'sorry {guests.pop()}, i could not invite you to my party.')
print(f'hi {guests[0]}, you will to my party.')
print(f'hi {guests[1]}, you will to my party.')

del guests[-1]
del guests[-1]

print(f'guests.length = {len(guests)}, nobody!')
