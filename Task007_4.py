# Задача 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

import os
os.system("cls")

x = [True, False]
y = [True, False]
z = [True, False]
for i in x:
    for j in y:
        for k in z:
            print('Для x:', x[i])
            print('Для y:', y[j])
            print('Для z:', z[k])
            if (not(x[i] or y[j] or [k]) == (not x[i] and not y[j] and not z[k])):
                print(' Выражение истинно')
            else: 
                print(' Выражение ложно')