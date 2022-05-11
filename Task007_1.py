# Задача 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

import os
os.system("cls")

x = [True, False]
y = [True, False]
z = [True, False]
p = [True, False]

for i in range(0, 1):
    if(not(x[i] or y[i] or z[i])) == (not x[i] and not y[i] and not z[i]):
        print(f'Выражение из условия - {p[i]}')
    else:
        print(f'Выражение из условия - {p[i+1]}')
