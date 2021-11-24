from itertools import count, cycle

my_list_a = count(10, 2)
my_list_b = cycle('abc')

print(list(next(my_list_a) for _ in range(10)))
print(list(next(my_list_b) for _ in range(10)))

