with open('text_2.txt', 'r', encoding='utf-8') as f:
    line = f.readlines()
    print(f'Всего строк: {len(line)}')
    for index, value in enumerate(line, 1):
        num = len(value.split())
        print(f'Строка {index} содержит {num} слов.')

