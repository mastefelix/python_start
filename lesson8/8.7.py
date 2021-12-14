class Complex:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return f'{self.a} {"-" if self.b < 0 else "+"} {abs(self.b)}j'

    def __add__(self, other):
        print('Сумма: ')
        return Complex(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        print('Произведение: ')
        return Complex((self.a * other.a - self.b * other.b), (self.a * other.b + self.b * other.a))


num_1 = Complex(1, 2)
num_2 = Complex(3, 4)
print(num_1 + num_2)
print(num_1 * num_2)
