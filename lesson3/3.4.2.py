def my_func(x, y):
    for i in range(1, abs(y)):
        x *= x
    return 1 / x


print(my_func(float(input('Введите действительное положительное число x: ')),
              int(input('Введите целое отрицательное число y: '))))
