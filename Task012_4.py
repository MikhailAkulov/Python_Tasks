# Задача 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# review

import os
os.system("cls")

dictionary = {n: 3*n+1 for n in range(1, int(input('Введите число: '))+1)}
print(f"Словарь индекс-значений: {dictionary}")
