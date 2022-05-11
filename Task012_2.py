# Задача 12. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
# Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

import os
os.system("cls")

from random import randint
def get_dict(n):
    return {x: 3 * x + 1 for x in range(1, n + 1)}
n = randint(1, 20)
print(n)
print(get_dict(n))