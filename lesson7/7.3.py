class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Сумма клеток: ')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Разность клеток: ')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 else 'Вычитание невозможно!'

    def __mul__(self, other):
        print('Умножение клеток: ')
        return Cell(self.nums * other.nums)

    def __truediv__(self, other):
        print('Деление клеток: ')
        return Cell(self.nums / other.nums) if other.nums != 0 else 'Нельзя делить на ноль!'


cell_1 = Cell(28)
cell_2 = Cell(16)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 / cell_2)
print(cell_1.make_order(6))
