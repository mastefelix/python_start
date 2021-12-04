class Matrix:
    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        for i in self.lists:
            print(*i)

    def __add__(self, other):
        try:
            c = [[int(self.lists[i][j]) + int(other.lists[i][j]) for j in range(len(self.lists[i]))]
                 for i in range(len(self.lists))]
            return Matrix(c)
        except IndexError:
            return f'Матрицы разных размеров!'


matrix_1 = [[1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]]
matrix_2 = [[9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]]

m_1 = Matrix(matrix_1)
m_2 = Matrix(matrix_2)
m_1.__str__()
print(6 * '-')
m_2.__str__()
print(6 * '-')
(m_1 + m_2).__str__()
