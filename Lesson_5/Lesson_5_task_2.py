# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

with open('test_file.txt') as file:
    print(f'Here is the text:\n\n{file.read()}')
    file.seek(0)
    my_list = file.readlines()
    print(f'\nAmount of lines is {len(my_list)}\n')

    for i, item in enumerate(my_list):
        print(f'In line {i + 1} there are {len(item.split())} word(s).')
