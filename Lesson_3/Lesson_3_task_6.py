# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, н
# о каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# via function


def int_func(usr_words):
    return usr_words.title()


print(int_func(input('Please enter space separated words: ')))


# via lambda 1

user_req = input('Please enter space separated words: ')
words = lambda usr_words: usr_words.title()
print(words(user_req))


# via lambda 2

print((lambda usr_words: usr_words.title())(input('Please enter space separated words: ')))
