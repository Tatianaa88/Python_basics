# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел. Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к
# полученной ранее сумме и после этого завершить программу.


def func_sum(user_sum, user_list):
    for i in user_list:
        user_sum += int(i)
    print(user_sum)
    return user_sum


m_sum = 0

while True:
    user_numbers = input('Please enter space separated numbers. Enter "q" when done. ')
    new_list = user_numbers.split()
    if new_list[-1] == 'q':
        new_list.pop()
        m_sum = func_sum(m_sum, new_list)
        break
    else:
        m_sum = func_sum(m_sum, new_list)
