# Задача 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

import os
os.system("cls")

def multy(a):
    if a == 1:
        return 1
    
    return a * multy(a-1)

n = 4

print("Sequence for ")
for i in range(1, n+1):
    print(multy(i), end=' ')
