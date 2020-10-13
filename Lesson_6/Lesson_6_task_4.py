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
        return f'{self.name} is going.'

    def stop(self):
        return f'{self.name} has stopped.'

    def turn(self, direction):
        return f'{self.name} has turned {direction}.'

    def show_speed(self):
        return f'The current speed is {self.speed}.'


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'{self.speed}. {self.name} is speeding, please slow down.'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f"Your current speed is {self.speed}. You're speeding, please slow down."


class PoliceCar(Car):
    def police(self):
        if self.is_police is True:
            return f'This is a police car.'


auto_1 = Car(60, 'white', 'Volkswagen', False)
print(auto_1.go(), auto_1.show_speed())

auto_2 = TownCar(70, 'green', 'Reno', False)
print(f'{auto_2.go()}The current speed is {auto_2.show_speed()}')

auto_3 = WorkCar(50, 'red', 'BMW', False)
print(f'{auto_3.go()}The color is {auto_3.color}. {auto_3.show_speed()}')

auto_4 = PoliceCar(50, 'black', 'Mercedes', True)
print(auto_4.go(), auto_4.police())

auto_5 = SportCar(60, 'yellow', 'Lamborghini', False)
print(f'{auto_5.go()} The color is {auto_5.color}.')
