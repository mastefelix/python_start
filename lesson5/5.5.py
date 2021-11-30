with open('text_5.txt', 'w+', encoding='utf-8') as f:
    f.write(input('Введите числа через пробел: '))
    f.seek(0)
    print(sum(map(int, f.read().split())))
