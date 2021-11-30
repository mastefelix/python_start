salary = {}
with open('text_3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        salary[line.split()[0]] = float(line.split()[1])
    print('Меньше 20000 получают', end=': ')
    print(*list(key for key, values in salary.items() if values < 20000), sep=', ')
    print(f'Средняя зарплата сотрудников: {sum(salary.values()) / len(salary)}')
