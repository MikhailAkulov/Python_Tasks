# Задача 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

# review 

import os
from itertools import accumulate
import operator
import random
os.system("cls")

# n = random.randint(8, 16)               # Для рандомного указания числа
n = int(input('Введите число: '))         # Ввод числа с консоли

print('Набор произведений чисел:', *
      list(accumulate([x for x in range(1, n + 1)], operator.mul)), '\n')