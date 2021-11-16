month_num = int(input('Введите номер месяца: '))

month_list = ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь',
              'Октябрь', 'Ноябрь', 'Декабрь']
seasons = ['зимний', 'весенний', 'летний', 'осенний']
season = 0

if 1 <= month_num <= 2 or month_num == 12:
    season = seasons[0]
elif 3 <= month_num <= 5:
    season = seasons[1]
elif 6 <= month_num <= 8:
    season = seasons[2]
elif 9 <= month_num <= 11:
    season = seasons[3]

if season != 0:
    month = month_list[month_num - 1]
    print(f'{month} - это {season} месяц.')
else:
    print('Вы ввели некорректное значение.')
