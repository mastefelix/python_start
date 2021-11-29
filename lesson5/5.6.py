my_dict = {}
numbers = '1234567890 '

with open('text_6.txt', encoding='utf-8') as f:
    for line in f:
        name, hours = line.split(':')
        my_dict[name] = sum(map(int, ''.join([num for num in hours if num in numbers]).split()))
print(my_dict)
