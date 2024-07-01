"""
Напишите функцию для поиска подстроки в тексте.
Пусть она инициализируется искомой подстрокой и в вечном цикле принимает строки для поиска.
Если подстрока найдена, пусть генератор отдает обратно индекс подстроки в строке. Если не найдена — то значение -1.
def search(substr):
    # Your code here

finder = search("is")
next(finder)
assert finder.send("Now is better than never.") == 4
assert finder.send("Readability counts.") == -1



"""


def search(substr):
    i = -1
    while True:
        line = yield i
        i = line.find(substr)

finder = search("is")
assert finder.send("Now is better than never.") == 4
assert finder.send("Readability counts.") == -1
