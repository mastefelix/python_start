# a = 3
# # b = 10
# # i = 1
# #
# # while a < b:
# #     a = a + 0.1 * a
# #     i += 1
# #
# # print(f'Hа {i} день спортсмен достиг результата — не менее {b} км.')

firs_dist = int(input('Enter first distance: '))
fin_dist = int(input('Enter finally distance: '))
count_day = 1

while firs_dist < fin_dist:
    print(f'{count_day} day: {firs_dist:0.2f}')
    firs_dist *= 1.1
    count_day += 1

print(f'{count_day} day: {firs_dist:0.2f}')
