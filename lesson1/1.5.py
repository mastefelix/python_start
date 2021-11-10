profit = int(input('Введите сумму выручки: '))
cost = int(input('Введите сумму издержек: '))

if profit > cost:
    rent = (profit - cost) / profit
    print('Фирма работает в прибыль. \n'
          'Рентабльность выручки = ', rent)
    staff = int(input('Введите количество сотрудников фирмы: '))
    print('Прибыль в рассчете на одного сотрудника = ', (profit - cost) / staff)
else:
    print('Фирма работает в убыток')
