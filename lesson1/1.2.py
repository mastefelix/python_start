time = int(input('Введите время в секундах: '))

hh = time // 3600
mm = (time % 3600) // 60
ss = (time % 3600) % 60

print(f'{hh:02}:{mm:02}:{ss:02}')
