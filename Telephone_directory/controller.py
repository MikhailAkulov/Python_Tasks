import record_tel
import search_tel
import ui
import logger


def run():
    temp = ui.choice()
    if temp == 1:
        print('Добавление нового контакта в справочник')
        entry = record_tel.record()  # Запись в справочник
        logger.log_to_file(entry)
        run()
    if temp == 2:
        print('\nПоиска контакта в справочнике\n')
        entry = search_tel.search()  # Поиск в справочнике
        logger.reading_file(entry)
        run()
    if temp == 3:
        print('\nВывода всех контактов справочника\n\
              \n=== КОНТАКТЫ ТЕЛЕФОННОГО СПРАВОЧНИКА ===\n')
        logger.read_all_file()
        run()
    if temp == 4:
        print('\nРабота телефонного справочника завершена\n')
        exit
