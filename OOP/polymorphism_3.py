"""
Заведите протокол Validator, поддерживающий метод is_valid(obj).
 Пусть этот протокол реализуют два класса: TextValidator и ValueValidator.
TextValidator инициализируется коллекцией символов (алфавитом).
Его метод is_valid() должен возвращать True либо False для входной строки в зависимости от того,
содержатся ли все ее символы в алфавите.
ValueValidator инициализируется двумя целыми числами: min_val и max_val.
Его метод is_valid() должен возвращать True либо False для числа-аргумента в зависимости от того,
входит ли оно в указанные границы (включая границы).
 """
from typing import Protocol, List


class Validator(Protocol):
    def is_valid(self, obj):
        pass


class TextValidator:
    def __init__(self, alphabet: List[str]) -> None:
        self.alphabet = alphabet

    def is_valid(self, obj: List[str]) -> bool:
        for i in obj:
            if i not in self.alphabet:
                return False
        return True


class ValueValidator:
    def __init__(self, min_val: int, max_val: int) -> None:
        self.min_val = min_val
        self.max_val = max_val

    def is_valid(self, obj: int) -> bool:
        return self.min_val <= obj <= self.max_val
