# Задача 41. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# Пример:
# На сжатие:
# Входные данные:
# WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW
# Входные данные: 
# 12W1B12W3B24W1B14W

import os
os.system("cls")

with open('Task041_1.txt', 'w') as data:
    data.write('WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW')
    
with open('Task041_1.txt', 'r') as data:
    string = data.readline()

#string = 'WWWWWWWWWWWWBWWWWWWWWWWWWBBBWWWWWWWWWWWWWWWWWWWWWWWWBWWWWWWWWWWWWWW'
cout = 1
s = ""
for i in range(len(string)-1):
    if i <= len(string):
        if string[i] == string[i + 1]:
            cout += 1
    
        else:
            a = string[i]
            s+= str(cout) + string[i]
            #print(cout, string[i], end=' ')
            cout = 1
s+= str(cout) + string[i]
#print(cout, string[i], end=' ')
print(s)
#как перевести чтоб сохранить в файл
with open('Task041_1.txt', 'w') as data:
    data.write(s)