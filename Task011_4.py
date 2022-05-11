# Задача 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system("cls")

n = int(input('Введите число: '))
 
def get_degree(n):
    return [((-3)**i) for i in range(n)]
 
print(get_degree(n))