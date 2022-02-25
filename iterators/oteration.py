# lst = [1, 2, 3, 4, 5, 6]
# book = {'title': 'langories',
#         'author': 'King',
#         'year': '1998'}
# string = 'hello world'
#
#
# iterator = iter(book)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator)) # А вот тут уже будет ошибка StopIteration
from random import random


class RandomIterator:

    def __iter__(self): # нужно чтобы итерироваться
        return self

    def __init__(self,k):
        self.k = k
        self.i =0

    def __next__(self):
        if self.i<self.k:
            self.i +=1
            return random()
        else:
            raise StopIteration


for x in RandomIterator(5):
    print(x)
