# Задача 32. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности

import os
os.system("cls")

subs = list(map(int, input('Введите последовательность чисел через пробел: ').split()))
FinalList = []
for i in range (0, len(subs)):
    duplicate = 0
    for j in range(0, len(subs)):
        if i != j:
            if subs[i] == subs[j]:
                duplicate = 1
    if duplicate == 0:
        FinalList.append(subs[i])
print('Cписок неповторяющихся элементов исходной последовательности:', FinalList)