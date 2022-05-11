# Задача 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system("cls")

list = []
N = int(input('Введите количество членов последовательности: '))
for i in range(N):
    if i % 2 == 0:
        list.append(3**i)
    else:
        list.append(-3**i)
print(list)