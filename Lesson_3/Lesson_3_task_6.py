# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.
# Продолжить работу над заданием. В программу должна попадать строка из слов, разделенных пробелом.
# Каждое слово состоит из латинских букв в нижнем регистре. Сделать вывод исходной строки, н
# о каждое слово должно начинаться с заглавной буквы. Необходимо использовать написанную ранее функцию int_func().

# via function

def int_func(usr_words):
    words = usr_words.title()
    return words


user_request = input('Please enter space separated words: ')
print(int_func(user_request))


# via lambda
user_req = input('Please enter space separated words: ')


words = lambda usr_words : usr_words.title()
print(words(user_req))
