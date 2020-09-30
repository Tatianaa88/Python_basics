# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def user_data(name, last_name, year_birth, city, email, phone):
    personal_data = f'The user name is {name}, last name is {last_name}, year of birth is {year_birth},' \
        f' city is {city}, email is {email}, phone is {phone}.'
    return personal_data


print(user_data(name='Anna', last_name='Aneeva', year_birth=1900,
                city='Anapa', email='anna.anapa@bk.ru', phone=1111111111))
