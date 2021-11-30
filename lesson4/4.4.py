from random import randint

my_list = [randint(0, 10) for _ in range(0, 10)]
un_list = filter(lambda i: (my_list.count(i) == 1), my_list)
print(my_list)
print(list(un_list))
