#5. Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью, вычислите рентабельность выручки
# (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчете на одного сотрудника.

takings = int(input('Please a total amount of takings: '))
costs = int(input('Please enter a total amount of costs: '))

if takings > costs:
    amn_empl = int(input('How many employees are there in the company? '))
    profit = round(takings - costs, 2)
    ratio = round(takings / costs, 2)
    print(f'Takings are {ratio} times bigger than costs. The profit per employee is {round(profit/amn_empl, 2)} USD.')

elif takings == costs:
    print('There is neither profit nor loss.')

elif takings < costs:
    loss = costs - takings
    print(f'The company loss is {loss}')