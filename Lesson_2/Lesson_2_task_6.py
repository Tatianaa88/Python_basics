# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

items_list = []
product_desc = {}
n = 1

while True:
    user_choice = input('Would you like to enterук products (y/n)? ').lower()

    if user_choice == 'n':
        print('Good buy')
        break
    if user_choice == 'y':
        product = input('Please enter product: ')
        price = input('Please enter price: ')
        quantity = input('Please enter quantity: ')
        unit_measure = input('Please enter units of measure: ')
        product_desc.update({"item": product, "price": price, "quantity": quantity, "units of measure": unit_measure})
        item_desc = product_desc
        item = (n,item_desc)
        n += 1
        items_list.append(item)
        print(items_list)
        continue
    else:
        print(f'You entered "{user_choice}" when "y" or "n" are expected.')
        continue

