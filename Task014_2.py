# Задача 14. Подсчитать сумму цифр в вещественном числе.

import os
os.system("cls")

string_number = str(float(input('Enter a real number: '))).replace('.', '')
list_number = [int(a) for a in string_number]
print(f'Sum of all digits in the real number is {sum(list_number)}.')