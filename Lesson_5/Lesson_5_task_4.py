# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.


with open('file_l5.txt') as file:
    my_list = file.readlines()
    for i in my_list:
        if i.split()[-1] == '1':
            with open('new_file_l5.txt', 'w') as n_file:
                n_file.write('Один — 1\n')
        if i.split()[-1] == '2':
            with open('new_file_l5.txt', 'a') as n_file:
                n_file.write('Два — 2\n')
        if i.split()[-1] == '3':
            with open('new_file_l5.txt', 'a') as n_file:
                n_file.write('Три — 3\n')
        if i.split()[-1] == '4':
            with open('new_file_l5.txt', 'a') as n_file:
                n_file.write('Четыре — 4\n')
with open('new_file_l5.txt') as new_file:
    print(new_file.read())
