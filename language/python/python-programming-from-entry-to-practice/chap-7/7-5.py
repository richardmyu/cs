prompt = "\nHow old are you? "
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    age = input(prompt)
    if int(age) < 3:
        print("free")
    elif int(age) >= 3 and int(age) <= 12:
        print("$ 10")
    elif int(age) > 12 and int(age) <= 120:
        print("$ 12")
    elif int(age) < 0 or int(age) > 120:
        continue
    if age == 'quit':
        break
