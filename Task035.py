# Задача 35. В файле находится N натуральных чисел, записанных через пробел.
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1].
# Найдите это число.

import os
os.system("cls")

file = open('Task035_numbers.txt', 'w')
file.write('0 1 2 3 4 5 6 8 9 10 11 12 13')

file = open('Task035_numbers.txt', 'r')

strnumbers = file.readline()
print('Исходная последовательность натуральных чисел: ',strnumbers)

splitnum = strnumbers.split()

for i in range(0, len(splitnum)):
    if int(splitnum[i]) + 1 != i + 1:
        findnum = i
        break

print('Отсутствующее число: ',findnum)

file.close