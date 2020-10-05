# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

from sys import argv
param = argv[1:]

if 'h' in param:
    print('h - help\n1st parameter - amount of hours\n2nd parameter - pay per hour\n3rd parameter - bonus')
else:
    income = int(param[0]) * int(param[1]) + int(param[2])
    print(income)
