# Задача 11. Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

import os
os.system("cls")

def power(s):
    """
    Function will get power of number -3
    """
    new = (-3) ** s

    return new

n = 5
spisok=[]

for i in range(n):
    spisok.append(power(i))

print(f"List of elements: {spisok}")
