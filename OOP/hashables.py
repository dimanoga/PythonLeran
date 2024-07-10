class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, person_obj):
        return isinstance(person_obj, Person) and self.name == person_obj.name


p1 = Person('IVAN')
p2 = Person('IVAN')
print(p1 == p2)
print(hash(p1))
print(hash(p2))


d = {p1:'Ivanov Ivan'}
print(d.get(p1))