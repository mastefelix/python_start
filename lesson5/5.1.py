with open('txt_1.txt', 'w', encoding='utf-8') as f:
    while True:
        s = input('')
        if s != '':
            f.write(f'{s}\n')
        else:
            break
