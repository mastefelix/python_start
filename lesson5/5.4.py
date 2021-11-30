rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('text_4_1.txt', 'w', encoding='utf-8') as f_new:
    with open('text_4.txt') as f:
        f_new.writelines([line.replace(line.split()[0], rus.get(line.split()[0])) for line in f])
