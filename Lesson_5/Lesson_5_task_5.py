# 5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

import random

file = open('random_numbers.txt', 'w')
file.close()

for i in range(6):
    with open('random_numbers.txt', 'a') as r_n:
        r_n.write(str(random.randint(1, 200)) + ' ')

with open('random_numbers.txt') as file:
    print(f'Here are the numbers: {file.read()}\n')
    file.seek(0)
    total_sum = 0
    for i in file.read().split():
        total_sum += int(i)
    print(f'Here is the sum of the numbers {total_sum}.')
