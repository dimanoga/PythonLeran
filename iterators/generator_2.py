"""Напишите генератор even_sequence(), который при каждом обращении генерирует положительные четные числа, начиная с 0. """


def even_sequence() -> int:
    number = 0
    while True:
        yield number
        number += 2
