from random import random


def simple_generator():
    print("check 1")
    yield 1
    print("check 2")
    yield 2
    print("check 3")

gen = simple_generator()
x = next(gen)
print(x)
print(next(gen))
print(next(gen))
# print('__________________________________')

# def random_generator(k):
#     for i in range(k):
#         yield random()
#
#
# gen = random_generator(3)
#
# for i in gen:
#     print(i)
