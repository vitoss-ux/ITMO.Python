import time
from random import randint

counter1 = []
counter2 = []


# Ввод имени
def name_input():
    player1 = input('Имя первого игрока: ')
    player2 = input('Имя второго игрока: ')
    return player1, player2


# Логика игры
def game_core(player1, player2):
    attempt = int(input('Ведите количество бросков для игрока: '))

    # Бросок первого игрока
    print('Кубик бросает ', player1)
    time.sleep(2)

    for i in range(attempt):
        counter1.append(randint(1, 6))

    print('Выпало: ', counter1)
    print('Сумма очков игрока ' + player1 + ': ', sum(counter1))

    # Бросок второго игрока
    print('Кубик бросает ', player2)
    time.sleep(2)

    for i in range(attempt):
        counter2.append(randint(1, 6))
    print('Выпало: ', counter2)
    print('Сумма очков игрока ' + player2 + ': ', sum(counter2))
    return [counter1, counter2]


# Победитель
def winner(player1, player2):
    if counter1 > counter2:
        print('Победил: ', player1)
    elif counter2 > counter1:
        print('Победил: ', player2)
    else:
        print('Победила дружба!')
