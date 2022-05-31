# Задача 17. Задать список из N элементов, заполненных числами из [-N, N]. 
# Найти произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число

# review

N = int(input('Введите число' + '\n'))
list = [i for i in range(-N,N+1)]
path = 'positions.txt'
data = open(path,'r')
count = 1
for line in data:
    if int(line) > len(list)-1:
        count*=1
    else:    
        count *= list[int(line)]
print(count)
data.close()
