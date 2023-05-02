from exa_12 import EmployeeFactory


def main():
    emps = [
        EmployeeFactory.create('M', '曹老板'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]

    for emp in emps:
        print('%s: %.2f元' % (emp.name, emp.get_salary()))


if __name__ == '__main__':
    main()
