class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("From get_name()")
        return self._name

    @name.setter
    def name(self, value):
        print('From set_name()')
        self._name = value

    # name = property(fget=get_name, fset=set_name)
    # name = property()
    # name = name.getter(get_name)
    # name = name.setter(set_name)


p = Person('Dima')
print(dir(p))
print(p.name)
p.name = 'Ivan'
