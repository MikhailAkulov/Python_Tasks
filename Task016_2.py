# Задача 16. Задать список из n чисел последовательности (1+1n)n и вывести на экран их сумму

# review

import os
import random
os.system("cls")

n = random.randint(1, 21)

num = [1+(1/i)**i for i in range(1, n+1)]
print('Заданный список из', n,
      'чисел последовательности:\n', num, '\nСумма чисел последовательности =', round(sum(num), 2), '\n')
