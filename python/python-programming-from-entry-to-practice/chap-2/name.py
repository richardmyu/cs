# -*- coding: utf-8 -*-

name = "ada lovelace"

# 2-3
print(f'Hello {name.title()}, would you like to learn some python today?')

# 2-4
print(name.title())
print(name.upper())
print(name.lower())

# 2-5/6
famous_person = 'albert Einstein'
message = 'once said, "A person who never made a mistake never tried anything new.'
print(f'{famous_person.title()} {message}')

# 2-7
strip_name = ' \talbert \n\t '
print("[" + strip_name.rstrip() + "]")
print("[" + strip_name.lstrip() + "]")
print("[" + strip_name.strip() + "]")

print(len(strip_name.rstrip()))
print(len(strip_name.lstrip()))
print(len(strip_name.strip()))
