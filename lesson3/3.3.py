def my_func():
    a, b, c = int(input('Введите число: ')), int(input('Введите число: ')), int(input('Введите число: '))
    li = [a, b, c]
    li.remove(min(li))
    return li[0] + li[1]


print(my_func())
