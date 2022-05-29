# Задача 41. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные:
# 12W1B12W3B24W1B14W

import itertools
import re
import os
os.system("cls")

def compress(text):
    for char, same in itertools.groupby(text):
        count = sum(1 for _ in same)
        yield str(count) + char if count == 1 else str(count)+char

with open('Task041_4(1).txt', 'w') as data:
    data.write(
        "WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW")

data = open('Task041_4(1).txt', 'r')
for line in data:
    compression = ''.join(compress(line))
data.close()

with open('Task041_4(2).txt', 'w') as data:
    data.write(compression)

data = open('Task041_4(2).txt', 'r')
for line in data:
    n = re.findall(r'\d+\D', line)

for line in n:
    i = 0
    n_int = re.findall(r'\d+', line)
    n_int = list(map(int, n_int))

    while n_int[i] != 0:
        n_str = re.findall(r'\D', line)
        n_int[i] = n_int[i] - 1
        string = "".join(n_str)
        print(string, end='')
data.close()