class Employee:
    def __init__(self, lastname, firstname, annual_salarys):
        self.lastname = lastname
        self.firstname = firstname
        self.annual_salary = annual_salarys

    def give_raise(self, money=5000):
        self.annual_salary = int(self.annual_salary) + int(money)
