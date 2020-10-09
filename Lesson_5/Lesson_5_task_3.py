# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

salary_2 = []
with open('salary.txt') as file:
    my_list = file.readlines()
    for i in my_list:
        if int((i.split()[1])) > 20000:
            salary_2.append(i.strip())
    print(f'Employees with the salary more than 20 000 USD: {" ,".join(salary_2)}.')
    for i in my_list:
        avrg_salary =

