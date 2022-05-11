# Задача 15. Написать программу получающую набор произведений чисел от 1 до N.
# Пример: пусть N = 4, тогда
# [ 1, 2, 6, 24 ]

import os
os.system("cls")

N = int(input('Enter a number of terms: '))


def factorial(N):
    if N == 0:
        return 1
    else:
        x = N * factorial(N - 1)
        print(f'{x}')
        return x

factorial(N)