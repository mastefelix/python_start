my_list = [8, 7, 7, 5, 3, 3, 3, 2]
new = int(input('Введите натуральное число: '))
i = 0

for n in my_list:
    if new <= n:
        i += 1
    else:
        break

my_list.insert(i, new)
print(my_list)
