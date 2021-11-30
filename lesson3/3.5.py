def my_func():
    s = 0
    while True:
        my_list = input('Вводите числа через пробел. Для выхода введите "Q": ').split()
        for i in my_list:
            if i.upper() != 'Q':
                try:
                    s += int(i)
                except ValueError:
                    print('Для выхода введите Q')
            else:
                return s
                break
        print(s)


print(my_func())
