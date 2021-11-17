month_num = int(input('Введите номер месяца: '))

month_dict = {1: 'Январь', 2: 'Февраль', 3: 'Март', 4: 'Апрель',
              5: 'Май', 6: 'Июнь', 7: 'Июль', 8: 'Август',
              9: 'Сентябрь', 10: 'Октябрь', 11: 'Ноябрь', 12: 'Декабрь'}
season = 0

if 1 <= month_num <= 2 or month_num == 12:
    season = 'зимний'
elif 3 <= month_num <= 5:
    season = 'весенний'
elif 6 <= month_num <= 8:
    season = 'летний'
elif 9 <= month_num <= 11:
    season = 'осенний'

if season != 0:
    print(f'{month_dict[month_num]} - это {season} месяц')
else:
    print('Вы ввели некорректное значение.')

