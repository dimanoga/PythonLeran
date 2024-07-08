class Person:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f'Hello from {self.name}')



class Student(Person):
    pass


s = Student('Ivan')
s.hello()
