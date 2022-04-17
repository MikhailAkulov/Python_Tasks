# Найти максимальное из пяти чисел

import os
os.system("cls")

massive = [12,32,16,8,14]
print(massive)
print('наибольшее число: ', max(massive))   # первый способ
max = massive[0]
for i in massive:
    if i>max:
        max=i
print('наибольшее число: ', max,'\n')   # второй способ