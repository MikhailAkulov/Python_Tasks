# Вывести на экран числа от -N до N

num = abs(int(input('введите число: ')))
for i in range(-num, num+1):
    print(i, end=' ')