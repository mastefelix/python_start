def fact(n):
    f = 1
    for i in range(n + 1):
        yield f'{i}! = {f}'
        f *= i + 1


for num in fact(int(input('Enter number: '))):
    print(num)

