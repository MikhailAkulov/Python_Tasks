# Задача 30.
# Вычислить число c заданной точностью d
# Пример
# при d = 0.001, π = 3.141      10^(-1)≤d≤10^(-10)

import os
os.system("cls")

import math
p = 0.0001
p = str(p).split('.')
L = len(p[1])
M = str(math.pi)
print(float(M[:L+2]))