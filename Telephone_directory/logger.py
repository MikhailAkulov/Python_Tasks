from datetime import datetime
import output_format

def log_to_file(entry):  # Запись в файл
    
    with open('horizontal_view.csv', 'a') as file:
        file.write(
            f'{entry[0]};{entry[1]};{entry[2]};{entry[3]};{entry[4]};\n')

    with open('vertical_view.csv', 'a') as file:
        file.write(
            f'{entry[0]}\n{entry[1]}\n{entry[2]}\n{entry[3]}\n{entry[4]}\n\n')    

def reading_file(param): # Чтение из файла
    b = output_format.format()
    if b == 1:
        with open('horizontal_view.csv', 'r') as file:
            for line in file:
                if param in line:
                    print(line)
    if b == 2:
        list = []
        with open('vertical_view.csv', 'r') as file:
            for line in file:
                if param in line:
                    list = line.split(";")
                    print(f'{list[0]}\n{list[1]}\n{list[2]}\n{list[3]}\n{list[4]}\n\n')                       

def read_all_file(): # Чтение всего справочника
    b = output_format.format()
    if b == 1:
        with open('horizontal_view.csv', 'r') as file:
            for line in file:
                print(line)    
    if b == 2:
        with open('vertical_view.csv', 'r') as file:
            for line in file:
                print(line)