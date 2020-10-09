# 1. Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
# Об окончании ввода данных свидетельствует пустая строка.

user_request = 'empty'
file = open('text.txt', 'w')
file.close()

while user_request != '':
    user_request = input('Please enter string to add to a file: ')
    with open('text.txt', 'a') as file:
        file.write(user_request + '\n')

with open('text.txt') as file:
    print(file.read())
