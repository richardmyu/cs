current_users = ['bob', 'Kvein', 'stuart', 'admin', 'superadmin']
new_users = ['jack', 'tom', 'Stuart', 'kvein', 'phil']

for user in new_users:
    if user.lower() in [val.lower() for val in current_users]:
        print(f'sorry, {user} this name is exists, please get another one.')
    else:
        print(f'great, {user} this name is not use')
