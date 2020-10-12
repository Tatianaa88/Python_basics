# 2. Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
# Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом, т
# олщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def cover_mass(self):
        mass = self.length * self.width
        return mass


one_meter_mass = 25
amnt_layers = 5

asphalt_square = Road(20, 5000)
asphalt_mass = (asphalt_square.cover_mass() * one_meter_mass * amnt_layers) / 1000
print(f'Total asphalt mass is {int(asphalt_mass)} t.')
