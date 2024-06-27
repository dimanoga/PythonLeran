"""Проведите рефакторинг класса TestClass: - Исправьте ошибки в объявлении инициализатора.
- Сделайте instance_method() методом объекта, class_method() методом класса, а static_method() статическим методом.
- Почините консольный вывод поля класса и поля объекта."""


class TestClass:
    class_field = "This is class field"

    def __init__(self):
        print("Constructor")
        self.instance_field = "This is instance field"

    def instance_method(self):
        print(f"Instance method. {self.instance_field}. {type(self).class_field}")

    @classmethod
    def class_method(cls):
        print(f"Class method. {cls.class_field}")

    @staticmethod
    def static_method():
        print("Static method")


tc = TestClass()

tc.instance_method()
tc.class_method()
tc.static_method()

TestClass.class_method()
TestClass.static_method()
