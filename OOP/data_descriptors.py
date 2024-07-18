from time import time

# Так  делать плохо из-за увеличения счетчика ссылокк == утечак
class IntDescriptor:
    def __init__(self):
        self._values = {}

    def __get__(self, instance, owner_class):
        if instance is None:
            return self
        return self._values.get(instance)

    def __set__(self, instance, value):
        self._values[instance] = value


class Vector:
    x = IntDescriptor()
    y = IntDescriptor()


v = Vector()
v.x = 5
v.y = 66
print(v.x)
