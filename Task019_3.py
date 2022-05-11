# Задача 19. Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

import os
os.system("cls")

# x(n+1) = (a*x(n)+b) % n

m = 100
b = 3
a = 2
x = 1
c = 50

list = []
for i in range(c):
    x = (a*x+b) % m
    list.append(x)
print(list)