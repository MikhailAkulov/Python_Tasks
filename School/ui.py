from get_push_data import get_data
from add_data import add_data


def operations():
    print('Выберите действие: \n1 - посмотреть информацию об учениках \n2 - добавить ученика\n3 - выход из программы\n')
    a = input('Введите соответствующую цифру: ')
    while True:
        if a == '1':
            print(*get_data())
            operations()
        if a == '2':
            add_data()
            operations()
        if a == '3':
            print('Работа завершена.')
            exit()
