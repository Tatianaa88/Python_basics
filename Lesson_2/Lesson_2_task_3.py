# 3. Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).

# list solution

months = ['January', 'February', 'March', 'April',
          'May', 'June', 'July', 'August',
          'September', 'October', 'November', 'December']

while True:
    user_choice = int(input("Please enter a month's serial number: "))
    if user_choice > 12:
        print(f'You entered incorrect serial number: {user_choice}.')
    elif user_choice <= 12:
        print(f'Here is the month you selected: {months[user_choice - 1]}')
        break

# dictionary solution

months = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
          5: 'May', 6: 'June', 7: 'July', 8: 'August',
          9: 'September', 10: 'October', 11: 'November', 12: 'December'}

while True:
    user_choice = int(input("Please enter a month's serial number: "))
    if user_choice > 12:
        print(f'You entered incorrect serial number: {user_choice}.')
    elif user_choice <= 12:
        print(f'Here is the month you selected: {months.get(user_choice)}')
        break
