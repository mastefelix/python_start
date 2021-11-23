from sys import argv


def salary():
    try:
        time, rate, bonus = map(float, argv[1:])
        print(time * rate + bonus)
    except ValueError:
        print('Вводите три числа!')


salary()
