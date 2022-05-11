# Задача 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system("cls")

def sub (x):
    if x in [0,1]:
        return 1
    else:
        return sub (x-1)*-3
list = []
for N in range (1,6):
    list.append (sub(N)) # Добавление элемента в конец списка
print (list)