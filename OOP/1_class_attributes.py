"""Реализуйте класс ResponseStats, который считает статистику HTTP кодов ответа некоего сервиса.
Помимо инициализатора у него должно быть три метода:
add_response(), который принимает HTTP код.
response_count(). Он принимает HTTP код и возвращает для него накопленное количество ответов.
http_err_pct(). Метод без аргументов. Возвращает процент HTTP кодов с ошибками от общего количества ответов.
 Код с ошибкой — это HTTP статус от 400 и выше. """
from collections import defaultdict


class ResponseStats:
    def __init__(self):
        self._status_codes_count = defaultdict(int)

    def add_response(self, status_code: int):
        self._status_codes_count[status_code] += 1

    def response_count(self, status_code: int):
        return self._status_codes_count.get(status_code, 0)

    def http_err_pct(self):
        err_code_count = 0
        total_code_count = 0
        for k, v in self._status_codes_count.items():
            total_code_count += v
            if k >= 400:
                err_code_count += v
        if total_code_count == 0:
            return 0
        return (err_code_count / total_code_count) * 100



rs = ResponseStats()

rs.add_response(200)
rs.add_response(200)
rs.add_response(400)
rs.add_response(500)
print(rs.response_count(status_code=200))  # 2
print(rs.http_err_pct())  # 50
