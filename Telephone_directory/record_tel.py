from datetime import datetime


import datetime
def  record():
    entry=[]
    surname = input('\nВведите Фамилию: ')
    entry.append(surname.title())
    name = input('Введите Имя: ')
    entry.append(name.title())
    telefon = input('Введите номер телефона: ')
    entry.append(telefon)
    description = input('Введите комментарий: ')
    entry.append(description.title())
    dt = datetime.datetime.now()
    entry.insert(0,dt.strftime('%H:%M - %d.%m.%Y year'))
    print('Добавлена запись: ', entry)
    return entry