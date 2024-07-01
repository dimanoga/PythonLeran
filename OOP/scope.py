name = 'Ivan'


class Person:
    name = 'Dima'  # Локальная для класса

    def print_name(self):
        print(name)  # Глобальная, тк нет привязки к экземпляру  класса

    def print_self_name(self):
        print(self.name)

    @classmethod
    def change_class_name(cls, name):
        cls.name = name


p = Person()
p.print_name()
p.change_class_name('asas')
print(Person.name)
p.print_self_name()
