# Задача 39. Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
#   На столе лежит 2021 конфета.
#   Играют два игрока делая ход друг после друга.
#   Первый ход определяется жеребьёвкой.
#   За один ход можно забрать не более чем 28 конфет.
#   Все конфеты оппонента достаются сделавшему последний ход.
#   Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
#       a) Добавьте игру против бота
#       b) Подумайте, как наделить бота "интеллектом"

import random
import os
os.system("cls")


def get_comp_move():
    if player[2] == 1:
        move = random.randint(min_step, max_step)
    else:
        if max_step >= candys:
            move = candys
        else:
            move = candys % (max_step+1)
    return move


def get_max_step(max, can):
    return max if max < can else can


def get_input():
    error = True
    while error:
        input_type = input("Введите число 1 или 2: ")
        if input_type.isdigit() and (0 < int(input_type) < 3):
            error = False
            input_type = int(input_type)
        else:
            print("Ошибка ввода!")
    return input_type


def get_start(pl):
    print('Это игра в конфеты.\nВыберите режим игры: 1 - два игрока, 2- игра с ботом')
    player_type = get_input()
    if player_type == 1:
        pl[0] = "Игрок 1"
        pl[1] = "Игрок 2"
    else:
        pl[0] = "Игрок"
        pl[1] = "Бот"
        print(
            "\nИгра с ботом! Выберите уровень сложности.\n1 - Бот без интеллекта. 2 - Бот с интеллектом")
        pl[2] = get_input()


def get_candys():
    error = True
    while error:
        inp = input()
        if inp.isdigit() and (min_step <= int(inp) <= max_step):
            player_move = int(inp)
            error = False
        else:
            print(
                f"Ошибка! Введите целое число от {min_step} до {max_step}")
    return player_move


player = ['', '', 1]

get_start(player)

candys = 2021                           # число конфет на старте (по условию)
# candys = random.randint(10, 50)       # число конфет на старте (для проверки)
min_step = 1                            # минимальный ход (поусловию)
max_step = 28                           # макимальный ход (поусловию)
# max_step = 4                          # макимальный ход (для проверки)
count = 1

while candys > 0:
    max_step = get_max_step(max_step, candys)
    print(
        f"\nРаунд {count}. Конфет осталось {candys}\nХодит {player[0]}.\nВозьмите от {min_step} до {max_step} конфет")

    player_move = get_candys()

    candys -= player_move
    if not candys:
        print(f"Победил {player[0]}!")
        break

    max_step = get_max_step(max_step, candys)

    print(f"\nКонфет осталось: {candys}\nХодит: {player[1]}.")
    if player[1] == "Игрок 2":
        max_step = get_max_step(max_step, candys)
        print(f"Возьмите от {min_step} до {max_step} конфет")
        player_move = get_candys()
    else:
        player_move = get_comp_move()
        print(f"{player[1]} взял {player_move} конфет")

    candys -= player_move
    if not candys:
        print(f"Победил {player[1]}!")
        break

    count += 1