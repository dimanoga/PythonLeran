from datetime import datetime
import pytz

WHITE = '\033[00m'
GREEN = '\033[0;92m'
RED = '\033[1;31m'


class Account:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance
        self._history = []

    @staticmethod
    def _get_localized_time():
        return pytz.utc.localize(datetime.utcnow())

    def deposit(self, amount):
        self._balance += amount
        self.show_balance()
        self._history.append([amount, self._get_localized_time()])

    def withdrawn(self, amount):
        if self._balance > amount:
            self._balance -= amount
            print(f'Withdrraw from balance  {amount}')
            self._history.append([-amount, self._get_localized_time()])
        else:
            print('Not enough money')
        self.show_balance()

    def show_history(self):
        for amount, data in self._history:
            if amount > 0:
                transaction = 'deposit'
                color = GREEN
            else:
                transaction = 'withdrawn'
                color = RED
            print(f'{color} {amount} {WHITE} {transaction} on {datetime.astimezone(data)} ')

    def show_balance(self):
        print(f'Balance {self._balance}')


a = Account('Test', 200)
a.deposit(100)
a.withdrawn(100)
a.deposit(500)
a.withdrawn(10000)
a.show_history()
