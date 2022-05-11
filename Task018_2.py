# Задача 18. Реализовать алгоритм перемешивания списка

import os
os.system("cls")

from random import randint

array = [1,2,3,4,5,6,7,8,9,10]
print(f'Первоначальный вид массива:\n{array}')
for i in range(0,len(array)-1):
    swap=array[i]
    rnd=randint(i+1,len(array)-1)
    array[i]=array[rnd]
    array[rnd]=swap
print(f'Массив после перемешивания:\n{array}')