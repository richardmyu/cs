# -*- coding: utf-8 -*-


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odomerter_reading = 0

    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model

        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odomerter_reading) + ' miles on it.')

    def update_odometer(self, mileage):
        if mileage >= self.odomerter_reading:
            self.odomerter_reading = mileage
        else:
            print('You can\'t roll back an odometer!')

    def increment_odometer(self, miles):
        self.odomerter_reading += miles


class Battery:
    def __init__(self, battery_size=70):
        self.battery_size = battery_size

    def describe_battery(self):
        print('This car has a ' + str(self.battery_size) + '-kwh battery.')

    def get_ranger(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270

        msg = 'This car can go approximately ' + str(range) + ' miles on a full charge.'

        print(msg)

    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

            print('This car battery size has upgraded.')


class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

    def fill_gas_tank(self):
        print('This car doesn\'t need a gas tank!')


my_tesla = ElectricCar('tesla', 'model s', 2016)

print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_ranger()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_ranger()
