# Задача 10. Найти расстояние между двумя точками пространства

import os
os.system("cls")

from math import sqrt

def find(first, second):
    result = (second - first) * (second - first)
    return result

x1 = int(input('Введите координату X1' + '\n'))
y1 = int(input('Введите координату Y1' + '\n'))
x2 = int(input('Введите координату X2' + '\n'))
y2 = int(input('Введите координату Y2' + '\n'))
z1 = int(input('Введите координату Z1' + '\n'))
z2 = int(input('Введите координату Z2' + '\n'))
sum = (find(x1, x2) + find(y1, y2)+find(z1,z2))**0.5

print(f'Расстояние между точками в 3D пространстве = {round(sum,3)}')