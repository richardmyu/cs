# -*- coding: utf-8 -*-

def greet_user(name):
    """显示简单的问候语"""
    # hh
    print("Hello! " + name.title())


greet_user(input("What is your name? "))

print("\n --- 位置实参 --- ")


# 位置实参(按照顺序取值)
def describe_pet(animal_type, pet_name):
    """显示宠物信息"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")


describe_pet('hamster', 'harry')
describe_pet('dog', 'jack')
describe_pet('tom', 'cat')

print("\n --- 关键字实参 --- ")


# 关键字实参(传参的时候，指定形参名称赋值)
def describe_book(book_name, book_price):
    print("\nBook's name: " + str(book_name))
    print("Book's price: " + str(book_price))


describe_book(book_name='python入门', book_price=34.5)
describe_book(book_price=54.5, book_name='python进阶')

print("\n --- 默认值 --- ")


# 默认值(先列出没有默认值的形参，有默认值的形参要放后面)
def describe_person(person_name, person_class=1):
    print("\n" + person_name.title() + "'s class is " + str(person_class) + ' class')


describe_person('jack', 2)
describe_person('tom')
describe_person(person_class=4, person_name='frank')
describe_person(person_name='mark')
# describe_person()

print("\n --- 返回值 --- ")


# 返回值
def get_formatted_name(first_name, last_name):
    full_name = first_name + ' ' + last_name
    return full_name.title()


print(get_formatted_name('jimi', 'hendrix'))

print("\n --- 可选的实参 --- ")


# 可选的实参
def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()


print(get_formatted_name('jimi', 'hendrix', 'j'))

# test
while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' to any time to quit)")
    f_name = input("First name: ").lower()
    if f_name == 'q':
        break
    l_name = input("Last name: ").lower()
    if l_name == 'q':
        break
    formatted_name = get_formatted_name(f_name, l_name)
    print("\nHello, " + formatted_name + "!")

print("\n --- 传递列表test --- ")


# test
def print_models(unprinted_designs, completed_models):
    """
    :param unprinted_designs: [list]
    :param completed_models: [list]
    :return:
    """
    while unprinted_designs:
        cur_des = unprinted_designs.pop()
        print("Printing model: " + cur_des)
        completed_models.append(cur_des)


def show_completed_models(completed_models):
    print("\nThe following models have been printed: ")
    for completed_model in completed_models:
        print(completed_model)


unprinted_designs = ["iphone", "robot", "dod"]
completed_models = []
# 当 unprinted_designs 不可修改时或者不确定是否有其他用处时，可传递副本 [:]
# 创建副本，会有消耗，所以除非有充分理由使用副本外，其他情况都应该传递原始列表
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print("\n --- homework --- ")


# homework
def show_magicians(magicians):
    for magician in magicians:
        print("\nMagician's name is " + magician)


def make_great(magicians):
    for index in range(len(magicians)):
        """
        修改列表值，需要通过 list[num] = 'xx' 的方式
        即要修改的是 指定地址 内的值
        直接覆盖 list，是不会起作用的
        因为直接赋值，等价于将当前形参，开辟一个新的地址
        """
        magicians[index] = "the great " + magicians[index]


magicians = ['jack', 'mark', 'tom']
make_great(magicians)
show_magicians(magicians)

print("\n --- homework2 --- ")


# homework 2
def show_magicians(magicians):
    for magician in magicians:
        print("\nMagician's name is " + magician)


def make_great(magicians):
    for index in range(len(magicians)):
        magicians[index] = "the great " + magicians[index]
    return magicians


magicians = ['jack', 'mark', 'tom']

show_magicians(make_great(magicians[:]))
show_magicians(magicians)

print("\n --- 传递任意实参 --- ")


# 传递任意实参(*toppings 是空元组，所有参数都会放进来)
def make_pizza(*toppings):
    # print(toppings)
    print("\nMake a pizza with the following toopings: ")
    for topping in toppings:
        print("- " + topping)


make_pizza('pepperroni')
make_pizza('pepperroni', 'mushrooms', 'green peppers')

print("\n --- 位置实参 + 传递任意实参 --- ")


# 位置实参 + 传递任意实参
def make_pizza(size, *toppings):
    print("\nMake a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)


make_pizza(16, 'pepperoni')
make_pizza(12, 'pepperoni', 'mushrooms', 'green peppers')

print("\n --- 任意关键字实参 --- ")


# 任意关键字实参(**user_info 是空字典，将所有其他参数（键值对）封装进来)
def build_profile(first, last, **user_info):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    # print(user_info)
    for key, value in user_info.items():
        profile[key] = value
    return profile


user_profile = build_profile('alert', 'einstein', location='princeton', field='physics')
print(user_profile)

print("\n --- homework3 --- ")


# homework3
def sandwich_side(*sides):
    print("\nMake a sandwich with the following sides: ")
    for side in sides:
        print("- ", side)


sandwich_side('apple')
sandwich_side('apple', 'banana')
sandwich_side('apple', 'banana', 'orange')

print("\n --- homework4 --- ")

# homework4
user_profile = build_profile('min', 'yu', location='chengdu', field='IT', status=-1)
print(user_profile)

print("\n --- homework5 --- ")


# homework5
def make_car(maker, model, **car_info):
    car_profile = {}
    car_profile['maker'] = maker
    car_profile['model'] = model
    for key, value in car_info.items():
        car_profile[key] = value
    return car_profile


car = make_car('subaru', 'outback', color='blue', two_package=True)
print(car)
