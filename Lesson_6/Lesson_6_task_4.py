# 4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police
# (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is going.')

    def stop(self):
        print(f'{self.name} has stopped.')

    def turn(self, direction):
        print(f'{self.name} has turned {direction}.')

    def show_speed(self):
        print(f'The current speed is {self.speed}.')


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"Your current speed is {self.speed}. You're speeding, please slow down.")


class SportkCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"Your current speed is {self.speed}. You're speeding, please slow down.")


class PoliceCar(Car):
    pass
