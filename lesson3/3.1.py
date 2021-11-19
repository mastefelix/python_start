def my_func():
    a, b = int(input('Ведите первое число: ')), int(input('Введите второе число: '))
    try:
        return a / b
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'


print(my_func())
