"""Превратите класс Navigation (построения маршрутов) в абстрактный класс.
 Наследуйте от него 2 класса: CarNavigation для автомобильных маршрутов и TransitNavigation для маршрутов на общественном транспорте.
Определенные в производных классах методы должны выводить в консоль сообщение вида Имя класса.
Имя метода Пусть они ничего не возвращают.
class Navigation:
    def build_route(self, start, finish):

    def get_maneuvers(self):
        ..."""
from abc import ABC, abstractmethod


class Navigation(ABC):
    @abstractmethod
    def build_route(self, start, finish):
        """
        Creates route between start and finish coordinates.
        Returns route object or None in case if the route couldn't be found.
        """
        ...

    @abstractmethod
    def get_maneuvers(self):
        """
        Returns list of maneuvers on the last route.
        """
        ...


class CarNavigation(Navigation):
    def build_route(self, start, finish):
        print(self.__class__.__name__ + '. ', self.build_route.__name__)

    def get_maneuvers(self):
        print(self.__class__.__name__ + '. ', self.get_maneuvers.__name__)


class TransitNavigation(Navigation):
    def build_route(self, start, finish):
        print(self.__class__.__name__ + '. ', self.build_route.__name__)

    def get_maneuvers(self):
        print(self.__class__.__name__ + '. ', self.get_maneuvers.__name__)


car_navigation = CarNavigation()
car_navigation.build_route(1, 2)
car_navigation.get_maneuvers()
