# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов
# класса Matrix (двух матриц). Результатом сложения должна быть новая матрица.


class Matrix:
    def __init__(self, matrix_1):
        self.matrix = matrix_1

    def __str__(self):
        final_string = ''
        for my_list in self.matrix:
            for item in my_list:
                final_string += f'{item}  '
            final_string += '\n'
        return f'{final_string}'

    def __add__(self, other):
        if len(self.matrix) == len(other):
            for i, my_list in enumerate(self.matrix):
                if len(my_list) == len(other[i]):
                    for j in range(len(my_list)):
                        self.matrix[i][j] += other[i][j]
                else:
                    return 'Matrices are not of the same size.'
            return Matrix(self.matrix)
        else:
            return 'Matrices are not of the same size.'

    def __getitem__(self, item):
        return self.matrix[item]

    def __len__(self):
        return len(self.matrix)


matrx_1 = Matrix([[31, 22], [37, 43], [51, 86]])
print(matrx_1)
matrx_2 = Matrix([[32, 22], [38, 43], [58, 86]])
print(matrx_2)
print(matrx_1 + matrx_2)
