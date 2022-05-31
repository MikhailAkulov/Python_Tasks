# Задача 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# review (с рандомным указанием числа N)

import random
import os
os.system("cls")

n = random.randint(1, 10)
dictionary = {x: 3 * x + 1 for x in range(1, n + 1)}
print(f"Словарь индекс-значений числа {n}:\n{dictionary}")