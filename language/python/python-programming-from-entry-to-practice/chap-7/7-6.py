prompt = "\nPlease enter the ingredients of the pizza: "
prompt += "\n(Enter 'quit' when you are finished.) "
msg = ""
acitve = True

while acitve:
    msg = input(prompt)
    if msg != "quit":
        print(msg)
    else:
        acitve = False
