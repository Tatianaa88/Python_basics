class Cell:
    def __init__(self, cell):
        self.alveole = cell

    def __add__(self, other):
        return f'The sum is {self.alveole + other.alveole}'

    def __sub__(self, other):
        if self.alveole - other.alveole > 0:
            return f'The result of subtraction is: {self.alveole - other.alveole}'
        else:
            return 'No cells left.'

    def __mul__(self, other):
        return f'The result of multiplication is {self.alveole * other.alveole}'

    def __truediv__(self, other):
        return f'The result of multiplication is {int(self.alveole / other.alveole)}'

    def make_order(self, cells_amount):
        order = ''
        for i in range(self.alveole):
            if i % cells_amount == 0 and i != 0:
                order += '\n'
            order += '*'
        return order


cell_1 = Cell(16)
cell_2 = Cell(7)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(Cell.make_order(cell_1, 4))
