# Задача 31. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

import os
from math import pi
from random import*
os.system("cls")

n = randint(1, 101)
print('Заданное число = ', n)
list = []
i = 2  # Чтобы не входил первый простой множитель - единица
while i <= n:
    if n % i == 0:
        list.append(i)
        n = n/i
        i -= 1
    i += 1
print('Список простых множителей:', list)