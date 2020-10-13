# 3. Реализовать базовый класс Worker (работник), в котором определить атрибуты: name, surname, position (должность),
# income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
# например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
# В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
# (get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        total_income = int(self._income.get('wage')) + int(self._income.get('bonus'))
        return total_income


employee = Position('Tatiana', 'Ageeva', 'SDE 1', {'wage': 10000, 'bonus': 5000})
print(employee.get_full_name())
print(employee.position)
print(employee.get_total_income())


employee_1 = Position('Mikhail', 'Ageev', 'SDE 2', {'wage': 20000, 'bonus': 10000})
print(employee_1.get_full_name())
print(employee_1.position)
print(employee_1.get_total_income())
