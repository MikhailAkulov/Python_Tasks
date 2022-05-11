# Задача 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

import os
os.system("cls")

def text_find(a,b):
    """
    Function will find occurence of word in the text
    """
    count = 0
    i = 0
    while i <= len(a):
        if b in a[i: i+len(b)]:
            #print("Найдено повторение номер", count+1)
            count += 1
            i += len(b)
        else:
            i += 1
    return count

a = "a тесты тесты тессс тесты"
b = "тесты"

print(f"Count of first word in second phrase: {text_find(a,b)}")
print(f"Count of first word in second phrase: {text_find('аааааааааа','аа')}")