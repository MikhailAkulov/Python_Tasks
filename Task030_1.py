# Задача 30.
# Вычислить число c заданной точностью d
# Пример
# при d = 0.001, π = 3.141      10^(-1)≤d≤10^(-10)

import os
from math import pi
from random import*
os.system("cls")

d = randint(1, 10)
print('Точность вывода = ', d)

print('Число π = ', round(pi, d), '\n')