import math
import statistics
import random

help(math)
help(statistics)

# Список из 10 чисел
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(number)

a = sum(number)  # Сумма всех чисел списка
print(a)

b = sum(number)/len(number)  # Среднее значение
print(b)

c = statistics.median(number)  # Медиана
print(c)

d = statistics.stdev(number)  # Стандартное отклонение
print(d)

#  Список из rand чисел в диапазоне 0-100
num = []

for i in range(100):
    num.append(random.randint(1, 100))
print(num)

