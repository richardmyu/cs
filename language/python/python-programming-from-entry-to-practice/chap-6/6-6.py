favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python'}

persons = ['jen', 'bob', 'phil', 'kevin', 'jack']

for name in persons:
    if name in favorite_languages.keys():
        print(f'thank you {name}')
    else:
        print(f'welcome to our survey {name}')
