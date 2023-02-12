class Person(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # 访问器 - getter方法
    @property
    def name(self):
        return self._name

    # 访问器 - getter方法
    @property
    def age(self):
        return self._age

    # 修改器 - setter方法
    @age.setter
    def age(self, age):
        self._age = age

    def print_ino(self):
        print(f'name: {self._name} age: {self._age}')


def main():
    person = Person('王大锤', 12)
    person.print_ino()
    person.age = 22
    person.print_ino()

    # person.name = '白元芳'
    # AttributeError: can't set attribute


if __name__ == '__main__':
    main()
