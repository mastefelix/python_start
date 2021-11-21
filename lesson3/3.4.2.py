def my_func(x, y):
    for i in range(1, abs(y)):
        x *= x
    return round(1 / x, 6)


print(my_func(float(input('Введите действительное положительное число x: ')),
              int(input('Введите целое отрицательное число y: '))))
