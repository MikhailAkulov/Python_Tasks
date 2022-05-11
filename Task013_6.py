# Задача 13. Пользователь задаёт две строки. Определить количество вхождений одной строки в другой.

# Не работающая версия, см. следующую 

import os
os.system("cls")

# str1= input('First string: ')
# str2= input('Second string: ')

str1 = 'Python free 777 $$$ python free python python python $$$ python'
str2 = 'python free new $$$'

str_list = str1.lower().split()
substr_list = str2.lower().split()

# print('String: ' + str1)
# print('Substrings: ' + str2)
# print()
#
# for i in substr_list:
#     count = 0
#     for j in str_list:
#         count = str_list.count(i)
#     print(f'{i} found {count} times.')