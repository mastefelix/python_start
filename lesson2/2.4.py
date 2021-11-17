st = list(input('Введите предложение: ').split(' '))

for i in range(len(st)):
    print(f'{i + 1} {st[i][:11]}')
