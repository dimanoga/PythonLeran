class Person:
    def __init__(self, name):
        self.name = name


class Student(Person):
    def __init__(self, surname, name):
        super().__init__(name)
        self.surname = surname


s = Student('Ivan', 'Petrov')
s2 = Student('Dima', 'Sidorov')
print(s2.name, s2.surname)
print(s.name, s.surname)
