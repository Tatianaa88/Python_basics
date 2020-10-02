# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Реализовать вывод данных о пользователе одной строкой.


def user_data(name, last_name, year_birth, city, email, phone):
    return f'The user name is {name}, last name is {last_name}, year of birth is {year_birth}, city is {city}, ' \
        f'email is {email}, phone is {phone}.'


print(user_data(name='Anna', last_name='Aneeva', year_birth=1900,
                city='Anapa', email='anna.anapa@bk.ru', phone=1111111111))
