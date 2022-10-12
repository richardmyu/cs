# -*- coding: utf-8 -*-

prompt = "\nPlease enter the ingredients of the pizza: "
prompt += "\n(Enter 'quit' when you are finished.) "
msg = ""

while True:
    msg = input(prompt)
    if msg != "quit":
        print(msg)
    else:
        break
