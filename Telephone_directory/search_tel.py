def search():
    print('Укажите параметр поиска: \n\
        1 - Фамилия;\n\
        2 - Имя;\n\
        3 - Номер телефона;\n\
        4 - Комментарий.\n')
    a = int(input('Ваш выбор: '))
    if a == 1:
        entry = input('Введите Фамилию: ').title()
    if a == 2:
        entry = input('Введите Имя: ').title()
    if a == 3:
        entry = input('Введите номер телефона: ')
    if a == 4:
        entry = input('Введите комментарий: ').title()

    print('Поиск по параметру : ', entry)
    return entry
