# !/usr/bin/env python
# coding= utf-8
'''
Date           : 2023-02-13 23:03:59
Description    :
'''

class Person(object):
    """人"""

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍.' % self._name)

    def learn_language(self):
        if self._age >= 18:
            print('%s在学习 python.' % self._name)
        else:
            print('%s在学习 c++.' % self._name)


class Student(Person):
    """学生"""

    def __init__(self, name, age, grade):
        super().__init__(name, age)
        self._grade = grade

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s.' % (self._grade, self._name, course))


class Teacher(Person):
    """老师"""

    def __init__(self, name, age, title):
        super().__init__(name, age)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s.' % (self._title, self._name, course))


def main():
    stu = Student('张三', 15, '初三')
    stu.study('数学')
    stu.play()
    stu.learn_language()

    t = Teacher('李四', 19, '数学老师')
    t.teach('如何把大象放入冰箱')
    t.play()
    t.learn_language()


if __name__ == '__main__':
    main()
