# Задача 31. Задайте натуральное число N. 
# Напишите программу, которая составит список простых множителей числа N.

import os
os.system("cls")

N = int(input("Задайте натуральное число: "))
List = []
for i in range(2, N):
    while N % i == 0:
        List.append(i)
        N = N/i
    if N == 1:
        break

if len(List) == 0:
    print("Число является простым")
else:
    print("Cписок простых множителей:", List)