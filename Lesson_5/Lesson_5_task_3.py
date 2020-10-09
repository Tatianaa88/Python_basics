# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# Определить, кто из сотрудников имеет оклад менее 20 тыс.,
# вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.

salary_2 = []
total_salary = 0
with open('salary.txt') as file:
    my_list = file.readlines()
    print('Employees with the salary more than 20 000 USD: \n')
    for i in my_list:
        if int((i.split()[1])) < 20000:
            print(i.strip())
        total_salary += int(i.split()[1])
    print(f'\nAverage salary is: {total_salary / int(len(my_list))}')
