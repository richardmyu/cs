# -*- coding: utf-8 -*-

class Dog():
    """构造 Dog 类"""

    def __init__(self, name, age):
        """初始化 name and age"""
        self.name = name
        self.age = age

    def sit(self):
        """下蹲"""
        print(self.name.title() + " is now sitting")

    def roll_over(self):
        """打滚"""
        print(self.name.title() + " rolled over!")


my_dog = Dog('willie', 6)
print(my_dog.name)
my_dog.sit()


class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        self.gas_tank = 100

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, mileage):
        if mileage >= 0:
            self.odometer_reading += mileage
        else:
            print("You can't roll back an odometer!")

    def fill_gas_tank(self):
        print("This car has " + str(self.gas_tank) + "L gas tank.")


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.fill_gas_tank()

# 修改属性值
# 1.直接修改属性
my_new_car.odometer_reading = 22
my_new_car.read_odometer()

# 2.通过方法修改
my_new_car.update_odometer(24)
my_new_car.read_odometer()
# my_new_car.update_odometer(2)
# my_new_car.read_odometer()

# 3.通过方法，属性值递增
my_new_car.increment_odometer(10)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()


# my_new_car.increment_odometer(-100)
# my_new_car.read_odometer()

# 将实例用作属性
class Battery():
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print("This car is has " + str(self.battery_size) + '-kWh battery.')

    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        msg = "This car can go approximately " + str(range)
        msg += " miles on a full change"
        print(msg)

    def update_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85


# 继承
# 1.父类必须在当前文件，且子类前
# 2.父类必须被显示指定
class ElectricCar(Car):
    def __init__(self, make, model, year):
        # super() 关联父类和子类
        super().__init__(make, model, year)
        # self.battery_size = 70
        self.battery = Battery()
        del self.gas_tank

    def describe_battery(self):
        # print("This car has a " + str(self.battery.battery_size) + "-kWh battery.")
        self.battery.describe_battery()

    def fill_gas_tank(self):
        """
        覆盖父类同名方法
        """
        print("This car doesn't need a gas tank.")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
# print(my_tesla.gas_tank)
my_tesla.describe_battery()
# my_tesla.battery.describe_battery()
my_tesla.fill_gas_tank()
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()
