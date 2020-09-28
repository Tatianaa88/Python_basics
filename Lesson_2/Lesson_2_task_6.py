# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

items_list = []
n = 1

while True:
    user_choice = input('Would you like to enter products (y/n)? ').lower()
    if user_choice == 'n':
        break
    if user_choice == 'y':
        product = input('Please enter product: ')
        price = input('Please enter price: ')
        quantity = input('Please enter quantity: ')
        unit_measure = input('Please enter units of measure: ')
        product_desc = {}
        product_desc.update({"item": product, "price": price, "quantity": quantity, "units of measure": unit_measure})
        item = (n, product_desc)
        n += 1
        items_list.append(item)
        continue
    else:
        print(f'You entered "{user_choice}" when "y" or "n" are expected.')
        continue

while True:
    user_request = input('Would you like to get an overview (y/n)?')
    if user_request == 'n':
        print('Good buy')
        break
    elif user_request == 'y':
        items_group = []
        price_group = []
        amn_group = []
        unit_group = []
        for i in range(len(items_list)):
            items_group.append(items_list[i][1].get('item'))
            price_group.append(items_list[i][1].get('price'))
            amn_group.append(items_list[i][1].get('quantity'))
            unit_group.append(items_list[i][1].get('units of measure'))
            summary = {'item': items_group, 'price': price_group, 'quantity': amn_group, 'units of measure': unit_group}
        print('Here is your overview: \n ')
        print(summary)
        break
    else:
        print(f'You entered "{user_request}" when "y" or "n" are expected. Please try again.')
        continue
