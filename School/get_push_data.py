from calendar import c
from itertools import zip_longest
from unittest import result


def summa(a):
    result = ''
    for i in range(3):
        result += a[i]
    return result.replace('\n', '')+'\n'


def get_data():
    with open('students.csv', 'r') as students:
        students = students.readlines()

    with open('cabinet.csv', 'r') as cabinet:
        cabinet = cabinet.readlines()

    with open('adress.csv', 'r') as adress:
        adress = adress.readlines()
    list = [summa(i)for i in zip(students, cabinet, adress)]
    return list


def push_data(str):
    str = str.split(';')
    with open('students.csv', 'a') as students:
        for i in range(0, 5):
            students.write(str[i]+';')
        students.write('\n')
    with open('cabinet.csv', 'a') as cabinet:
        cabinet.write(str[0]+';')
        for i in range(5, 7):
            cabinet.write(str[i]+';')
        cabinet.write('\n')
    with open('adress.csv', 'a') as adress:
        adress.write(str[0]+';')
        for i in range(7, 12):
            adress.write(str[i]+';')
        adress.write('\n')
