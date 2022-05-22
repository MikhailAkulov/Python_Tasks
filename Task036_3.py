# Задача 36. Дан список чисел. 
# Создать список, в который попадают числа, описываемые возрастающую последовательность.
# Пример: 
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.
# Порядок элементов менять нельзя

from random import *
import os
os.system("cls")

nums = [randint(1, 9) for i in range(21)]
print('Задан список: ', nums)


def get_create(nums):
    ups = [nums[0]]
    for i in nums:
        if i > max(ups):
            ups.append(i)
    return ups


print('Последовательность: ', get_create(nums))

largest = 0
index = 0

for i in range(len(nums)):
    #     if len(get_create(nums[i:])) > largest:
    #         largest = len(get_create(nums[i:]))
    #         index = i
    print(get_create(nums[i:]))
# print('Итого, создан список: ', nums[index:])
# print('Итого, последовательность: ', get_create(nums[index:]), '\n')
