class ValidString:
    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        print('set')
        if not isinstance(value, str):
            raise ValueError(f"Property {self.name} must be a str. Given {type(value)}")
        # key = '_' + self.name
        # setattr(instance, key, value)
        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        print('get')
        if instance is None:
            return self
        key = '_' + self.name
        return instance.__dict__.get(self.name, None)


class Person:
    name = ValidString()
    surname = ValidString()


kek = Person()
kek.name = 'Ivan'
kek.surname = 'Petrov'
print(kek.name)
