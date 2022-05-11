# Задача 7. Проверить истинность утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат

import os
os.system("cls")


X = [True, False]
Y = [True, False]
Z = [True, False]
P = [True, False]

for i in range(0,1):
    if (not(X[i] or Y[i] or Z[i])) == (not X[i] and not Y[i] and not Z[i]):
        print (f'Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - {P[i]}')
    else:
        print (f'Выражение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z - {P[i+1]}')