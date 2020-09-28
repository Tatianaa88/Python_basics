# 2. Для списка реализовать обмен значений соседних элементов,
# т.е. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input().

user_num = 0
user_list = []

while True:
    user_num = input('Please enter a number. When done type in "q": ')
    if user_num == 'q':
        break
    elif user_num.isdigit():
        user_list.append(int(user_num))
    else:
        print('Your input is not correct.')

print(f'Here is your original list: {user_list}')

for i in range(len(user_list)):
    if i % 2 != 0:
        user_list[i], user_list[i - 1] = user_list[i - 1], user_list[i]
print(f'Here is your modified list: {user_list}')
