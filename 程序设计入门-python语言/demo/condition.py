# -*- coding: utf-8 -*-

# for 语句
cars = ["audi", "bmw", "subaru", "toyota"]
for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

msg = "Hello world"
# 首字母大写
print(msg.title())
# 大写
print(msg.upper())
# 小写
print(msg.lower())
# 都不改变
print(msg)

# == & ！=
# 不同类型不等
print(1 == 2)
print(1 != 2)
print(1 != '2')
print(1 == '1')

# 多条件判断
print(1 <= 2 and 2 <= 3)
print(1 <= 2 or 2 >= 3)

# 值存在/不存在(in/not in)
balls = ["一星龙", "二星龙", "三星龙"]
print("一星龙" in balls)
print("二星龙" not in balls)

age = 12
if age < 4:
    print("you are a cute baby")
elif age < 18:
    print("you are a teenager ")
elif age < 69:
    print("you are a man or woman")
else:
    print("you are a old man")

for lit in range(1, 10):
    if lit == 1:
        print(str(lit) + 'st')
    elif lit == 2:
        print(str(lit) + 'nd')
    elif lit == 3:
        print(str(lit) + 'rd')
    else:
        print(str(lit) + 'th')

# while 语句
cur_num = 1
while cur_num <= 5:
    print(cur_num)
    cur_num += 1

prompt = "\nTell me something, i will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program."
msg = ""
# while msg != "quit":
#     msg = input(prompt).lower()
#     if msg != "quit":
#         print(msg)

# break
while True:
    msg = input(prompt).lower()
    if msg == "quit":
        break
    print(msg)

# continue
cur_num = 1
while cur_num <= 10:
    cur_num += 1
    if cur_num % 2 == 0:
        continue
    print('current-number ', cur_num)

# 使用 while 来处理列表和字典
# for 循环中不应当修改，否则难以跟踪
unconfirmed_users = ["alice", "brian", "candace"]
confirmed_users = []

while unconfirmed_users:
    cur_user = unconfirmed_users.pop()
    print("Verifying user: ", cur_user.title())
    confirmed_users.append(cur_user)
print("\nThe following users have been confirmed: ")
for conf_user in confirmed_users:
    print(conf_user.title())

# test
responses = {}
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    responses[name] = response
    repeat = input("Would you like to let another person respond?(yes/no)").lower()
    if repeat == 'no':
        polling_active = False
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name.title() + " would like to climb " + response + '.')

