def my_func(a, b):
    try:
        a, b = int(a), int(b)
        return round(a / b, 4)
    except ValueError:
        return 'Введите числа!'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'


print(my_func((input('Ведите первое число: ')), input('Введите второе число: ')))
