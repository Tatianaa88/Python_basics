#4. Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

usr_num = int(input('Please enter a random big number: '))
max_num = 0

while usr_num != 0:
    num = usr_num % 10
    usr_num = (usr_num - num)/10
    if num > max_num:
        max_num = num

print(round(max_num))

