profit = int(input('Введите сумму выручки: '))
cost = int(input('Введите сумму издержек: '))

if profit > cost:
    print(f'''Фирма работает в прибыль.
          Рентабельность выручки = {(profit - cost) / profit:.5}''')
    staff = int(input('Введите количество сотрудников фирмы: '))
    print(f'Прибыль в расчете на одного сотрудника = {(profit - cost) / staff:.5}')
else:
    print('Фирма работает в убыток')
