"""
Есть базовый класс Storage для хранения текстовых сообщений и их поиска по id. Наследуйте от него класс InMemoryStorage.
Пусть в инициализаторе он принимает дополнительный аргумент message_count_limit.
Если при добавлении нового сообщения через save_message() количество хранимых сообщений может превысить message_count_limit,
метод должен сгенерировать исключение с помощью конструкции raise Exception("Too many messages").
Если же длина сообщения превышает message_size_limit, метод должен сгенерировать исключение с текстом "Message is too long".
 Если сообщение с указанным id уже есть в хранилище, оно должно быть перезаписано.
Метод get_message() должен возвращать сообщение либо None, если оно не найдено.
Имплементируйте методы save_message() и get_message() таким образом, чтобы они расширяли функциональность Storage.
Код родительского класса должен выполняться в самом начале метода класса-потомка.

class Storage:
    def __init__(self, message_size_limit):
        self._message_size_limit = message_size_limit

    def save_message(self, message_id, message):
        print(f"Saving message {message_id}...")

    def get_message(self, message_id):
        print(f"Extracting message {message_id}...")
"""


class Storage:
    def __init__(self, message_size_limit):
        self._message_size_limit = message_size_limit

    def save_message(self, message_id, message):
        print(f"Saving message {message_id}...")

    def get_message(self, message_id):
        print(f"Extracting message {message_id}...")


class InMemoryStorage(Storage):
    def __init__(self, message_count_limit, message_size_limit):
        super().__init__(message_size_limit=message_size_limit)
        self._message_count_limit = message_count_limit
        self._messages = {}

    def save_message(self, message_id, message):
        if len(self._messages) >= self._message_count_limit:
            raise Exception('Too many messages')
        if len(message) > self._message_size_limit:
            raise Exception('Message is too long')
        super().save_message(message_id, message)
        self._messages[message_id] = message

    def get_message(self, message_id):
        super().get_message(message_id=message_id)
        return self._messages.get(message_id, None)


kek = InMemoryStorage(message_size_limit=10, message_count_limit=2)
kek.save_message(message_id=1, message='test1')
try:
    kek.save_message(message_id=2, message='TooLongMessage')
except Exception as e:
    print(e)
kek.save_message(message_id=2, message='test2')
try:
    kek.save_message(message_id=3, message='test3')
except Exception as e:
    print(e)
print(kek.get_message(message_id=1))
print(kek.get_message(message_id=10))
