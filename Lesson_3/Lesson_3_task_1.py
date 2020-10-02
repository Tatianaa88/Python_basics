# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.


def func_div(a, b):
    if b == 0:
        return 'Not'
    else:
        return a/b


user_num1 = int(input('Please enter number 1: '))
user_num2 = int(input('Please enter number 2: '))

div_result = func_div(user_num1, user_num2)
if div_result == 'Not':
    print('Division by 0 is not allowed.')
else:
    print(div_result)
