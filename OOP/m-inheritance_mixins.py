class FoodMixin:
    food = None

    def get_food(self):
        if self.food is None:
            raise ValueError
        print(f'I like {self.food}')


class Person:
    def hello(self):
        print('Hello from Person')


class Student(FoodMixin, Person):
    food = 'Pizza'

    def hello(self):
        print('Hello from Student')


s = Student()
s.hello()
s.get_food()
print(dir(s))
print(s.__class__.mro())
