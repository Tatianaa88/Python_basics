# 3. Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.

usr_num = input('Please enter a random number: ')

print(f'The sum of {usr_num} + {usr_num + usr_num} + {usr_num + usr_num + usr_num} = '
      f'{int(usr_num) + int(usr_num + usr_num) + int(usr_num + usr_num + usr_num)}')
