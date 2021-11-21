def my_func():
    a, b, c = input('Введите число: '), input('Введите число: '), input('Введите число: ')
    try:
        a, b, c = int(a), int(b), int(c)
        my_list = [a, b, c]
        my_list.remove(min(my_list))
        return sum(my_list)            # my_list[0] + my_list[1]
    except ValueError:
        return 'Вводите только числа!'


print(my_func())
