# Задача 34. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

# Создаем файлы с многочленами
first_file = open('task034_1.txt', 'w')
second_file = open('task034_2.txt', 'w')
example_1 = '16 * x ^ 3 + 23 * x ^ 2 + 24 * x + 5 = 0'
example_2 = '27 * x ^ 3 + 41 * x ^ 2 + 53 * x + 9 = 0'
first_file.write(example_1)
second_file.write(example_2)
first_file.close()
second_file.close()

file1 = open('task034_1.txt', 'r')
file2 = open('task034_2.txt', 'r')
strone = file1.readline()
strtwo = file2.readline()

resmass = []
polynom = ''

def splitter(str):
    str = str.replace(' ', '')
    mass = str.split('+')
    return mass

def createnum(mass):
    resmass = []
    for i in range(0, len(mass)):
        linex = ''
        line = mass[i]
        for i in range(0, len(line)):
            if line[i].isdecimal():
                linex += line[i]
            else:
                break
        resmass.append(linex)
    return resmass

def notequal(arr1, arr2):
    diff = (len(arr1) - len(arr2))
    for i in range(0, len(arr1)):
        if diff > 0:
            resmass.append(int(arr1[i]))
        else:
            resmass.append(int(arr1[i]) + int(arr2[-diff]))
        diff -= 1
    return resmass

massone = splitter(strone)
masstwo = splitter(strtwo)
massonefin = createnum(massone)
masstwofin = createnum(masstwo)

if len(massonefin) == len(masstwofin):
    for i in range(0, len(massonefin)):
        resmass.append(int(massonefin[i]) + int(masstwofin[i]))
elif len(massonefin) > len(masstwofin):
    resmass = notequal(massonefin, masstwofin)
elif len(massonefin) < len(masstwofin):
    resmass = notequal(masstwofin, massonefin)

for i in range(len(resmass) - 1, -1, -1):
    if i > 1:
        polynom += str(resmass[-(i + 1)]) + ' * x ^ ' + str(i) + ' + '
    elif i == 1:
        polynom += str(resmass[-(i + 1)]) + ' * x + '
    elif i == 0:
        polynom += str(resmass[-(i + 1)]) + ' = 0'

endpoly = open('task034_3.txt', 'w')
endpoly.write(polynom)
print('Коэффициенты первого многочлена:', massonefin)
print('Коэффициенты второго многочлена:', masstwofin)
print('Сумма многочленов:', polynom)
endpoly.close()