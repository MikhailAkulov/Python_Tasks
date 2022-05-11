# Задача 9. Указав номер четверти прямоугольной системы координат, показать допустимые значения координат для точек этой четверти

import os
os.system("cls")

quarter_number = int(input("Введите номер четверти: "))
if quarter_number == 1:
    print('x > 0, y > 0')
elif quarter_number == 2:
    print('x < 0, y > 0')
elif quarter_number == 3:
    print('x < 0, y < 0')
elif quarter_number == 4:
    print('x > 0, y < 0')
else:
    print(' В координатной плоскости всего 4 четверти')