# Задача 33. Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
import os
os.system("cls")

def isdigit(value):
    try:
        int(value)
        return True
    except ValueError:
        return False

while True:
    k = str(input('Задайте нарутальную степень k: '))
    if isdigit(k) and (int(k) != 0):
        k = int(k)
        break
    else:
        print('Ошибка! Введите цифру')

file = open("task033_1.txt", 'w+')
while k > 1:
    file.write(str(randint(1, 100)) + '*x^' + str(k) + '+')
    k -= 1
file.write(str(randint(1, 100)) + '*x+' + str(randint(1, 100)) + '=0')
file.close()