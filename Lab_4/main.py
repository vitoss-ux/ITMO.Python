# -------- Работа с оператором ветвления --------

import time
from random import randint

player1 = input('Имя первого игрока: ')
player2 = input('Имя второго игрока: ')

# Бросок первого игрока
print('Кубик бросает ', player1)
time.sleep(2)
n1 = randint(1, 6)
print('Выпало: ', n1)

# Бросок второго игрока
print('Кубик бросает ', player2)
time.sleep(2)
n2 = randint(1, 6)
print('Выпало: ', n2)

# Победитель
if n1 > n2:
    print('Победил: ', player1)
elif n1 < n2:
    print('Победил: ', player2)
else:
    print('Победила дружба!')

# -------- Использование циклов --------

attempt = int(input('Ведите количество бросков для игрока: '))

player1 = input('Имя первого игрока: ')
player2 = input('Имя второго игрока: ')

# Бросок первого игрока
print('Кубик бросает ', player1)

counter1 = []
for i in range(attempt):
    counter1.append(randint(1, 6))

print('Выпало: ', counter1)
print('Сумма очков игрока ' + player1 + ' ', sum(counter1))

# Бросок второго игрока
print('Кубик бросает ', player2)

counter2 = []
for i in range(attempt):
    counter2.append(randint(1, 6))
print('Выпало: ', counter2)
print('Сумма очков игрока ' + player2 + ' ', sum(counter2))

# Победитель
if counter1 > counter2:
    print('Победил: ', player1)
elif counter1 < counter2:
    print('Победил: ', player2)
else:
    print('Победила дружба!')
