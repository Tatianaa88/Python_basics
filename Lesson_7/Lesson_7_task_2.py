# 2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют параметры:
# размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
# Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def coat(self):
        pass

    @abstractmethod
    def suit(self):
        pass


class Clothes1(Clothes):
    def __init__(self, param):
        self.param = param
        self.total_amount = []

    @property
    def coat(self):
        return round(self.param / 6.5 + 0.5, 2)

    @property
    def suit(self):
        return round(self.param * 2 + 0.3, 2)


coat_1 = Clothes1(42)
print(f'Material for a coat: {coat_1.coat} m.')
suit_1 = Clothes1(100)
print(f'Material fot a suit: {suit_1.suit} m.')