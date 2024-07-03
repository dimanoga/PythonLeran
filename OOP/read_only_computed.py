class Person:
    def __init__(self, name, surname):
        self._surname = surname
        self._name = name
        self.__full_name = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value
        self.__full_name = None

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, value):
        self._surname = value
        self.__full_name = None

    @property
    def full_name(self):
        if self.__full_name is None:
            self.__full_name = f'{self._name} {self._surname}'
        return self.__full_name


p = Person('Ivan', 'Petrov')
print(p.name)
print(p.full_name)
p.name = 'Dima'
print(p.full_name)
print(p.full_name)
