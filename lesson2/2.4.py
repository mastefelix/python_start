st = list(input('Введите предложение: ').split(' ').remove(' '))

for i in range(len(st)):
    print(f'{i + 1} {st[i][:11]}')
