n = int(input('Введите целое положительное число: '))
min_n = 10
max_n = 0

while n > 0:
    if (n % 10) < min_n:
        min_n = n % 10
    if (n % 10) > max_n:
        max_n = n % 10
    n = n // 10

print(min_n, max_n)
