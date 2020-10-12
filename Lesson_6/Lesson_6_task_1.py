# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) —
# 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только
# в указанном порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.

from itertools import cycle
import time


class TrafficLight:
    def __init__(self, color):
        self.__color = color

    def running(self):
        for i in cycle(self.__color):
            print(i)
            if i == 'red' or i == 'green':
                time.sleep(7)
            else:
                time.sleep(2)


traffic_light = TrafficLight(['red', 'yellow', 'green'])
traffic_light.running()
