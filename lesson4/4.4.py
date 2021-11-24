from random import randint

my_list = [randint(0, 10) for _ in range(0, 10)]
un_list = [i for i in my_list if my_list.count(i) == 1]
print(my_list)
print(un_list)
