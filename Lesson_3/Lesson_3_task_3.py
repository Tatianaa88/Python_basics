# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(a, b, c):
    my_list = [a, b, c]
    for i in my_list:
        if min(my_list) < i < max(my_list):
            result = max(my_list) + i
            return result


print(my_func(3, 5, 6))
