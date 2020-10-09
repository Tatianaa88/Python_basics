# 7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
# название, форма собственности, выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]

import json

my_dict = {}
neg_dict = {}
profit_list = []
t_profit_s = 0

with open('overview.txt') as file:
    for f in file.readlines():
        if int(f.split()[-2]) >= int(f.split()[-1]):
            profit_list.append(str(int(f.split()[-2]) - int(f.split()[-1])))
            my_dict.update({f.split()[0]: int(f.split()[-2]) - int(f.split()[-1])})
        else:
            neg_dict.update({f.split()[0]: int(f.split()[-2]) - int(f.split()[-1])})
    for i in profit_list:
        t_profit_s += int(i)
    overview_list = [my_dict, neg_dict, {'average_profit': t_profit_s / len(profit_list)}]

with open("overview.json", "w") as new_jf:
    json.dump(overview_list, new_jf)
