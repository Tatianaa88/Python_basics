# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица измерения).
# Структуру нужно сформировать программно, т.е. запрашивать все данные у пользователя.

# items_list = []
#
# n = 1
#
# while True:
#     user_choice = input('Would you like to enterук products (y/n)? ').lower()
#
#     if user_choice == 'n':
#         print('Good buy')
#         break
#     if user_choice == 'y':
#         product = input('Please enter product: ')
#         price = input('Please enter price: ')
#         quantity = input('Please enter quantity: ')
#         unit_measure = input('Please enter units of measure: ')
#         product_desc = {}
#         product_desc.update({"item": product, "price": price, "quantity": quantity, "units of measure": unit_measure})
#         item_desc = product_desc
#         item = (n, item_desc)
#         n += 1
#         items_list.append(item)
#         print(items_list)
#         continue
#     else:
#         print(f'You entered "{user_choice}" when "y" or "n" are expected.')
#         continue

items_list = [(1, {'item': 'laptop', 'price': '2000', 'quantity': '4', 'units of measure': 'units'}),
              (2, {'item': 'scanner', 'price': '200', 'quantity': '5', 'units of measure': 'units'}),
              (3, {'item': 'printer', 'price': '200', 'quantity': '6', 'units of measure': 'units'})]

while True:
    user_request = input('Would you like to get an overview/analysis (y/n)?')
    if user_request == 'n':
        print('Good buy')
        break
    elif user_request == 'y':
        items_group = []
        price_group = []
        unit_group = []
        for i in range(len(items_list)):
            items_group.append(items_list[i][1].get('item'))
            price_group.append(items_list[i][1].get('price'))
            unit_group.append(items_list[i][1].get('units of measure'))
            analysis = {'item': items_group, 'price': price_group, 'units of measure': unit_group}
        print(f'Here is your overview: {analysis}')
        break
    else:
        print(f'You entered "{user_request}" when "y" or "n" are expected. Please try again.')
        continue



