"""Реализуйте класс-итератор KVIterator: обертку для итерирования по ключам и значениям словаря.

class KVIterator:
    def __init__(self, d):
        ...

d = {"a": 1, "b": 2}

for k, v in KVIterator(d):
    print(f"{k}={v}")
"""


class KVIterator:
    def __init__(self, d: dict):
        self._iter = iter(d.items())

    def __iter__(self):
        return self._iter

    def __next__(self):
        return next(self._iter)


d = {"a": 1, "b": 2}

for k, v in KVIterator(d):
    print(f"{k}={v}")
