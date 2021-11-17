goods = []
good = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analytics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0

while True:
    if input('Для продолжения нажмите "Enter", для выхода - "Q"').upper() == 'Q':
        break
    else:
        num += 1
        f_copy = good.copy()
        for f in good:
            prop = input(f"Введите {f}: ")
            f_copy[f] = int(prop) if f == 'цена' or f == 'количество' else prop
            analytics[f].append(f_copy[f])
        goods.append((num, f_copy))
        print(f'\nСтруктура товаров\n{goods}')
        print(f'\nТекущая аналитика:\n')
        for key, value in analytics.items():
            print(f'{key}: {value}')
