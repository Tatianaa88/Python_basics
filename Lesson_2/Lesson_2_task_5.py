# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

rating = [7, 5, 4, 4, 2]
print(f'Current rating is {rating}')

while True:
    user_rating = input('Please enter you rating from 1 to 9. When done enter "q". ')
    if user_rating == 'q':
        print('Good buy')
        break
    elif int(user_rating) >= rating[0]:
        rating.insert(0, int(user_rating))
        print(f'New rating is {rating}')
        continue
    elif int(user_rating) <= rating[-1]:
        rating.append(int(user_rating))
        print(f'New rating is {rating}')
        continue
    for i in range(len(rating)):
        if rating[i] == int(user_rating):
            rating.insert(i + 1, int(user_rating))
            print(f'New rating is {rating}')
            break
        elif rating[i] > int(user_rating) > rating[i + 1]:
            rating.insert(i + 1, int(user_rating))
            print(f'New rating is {rating}')
            break
