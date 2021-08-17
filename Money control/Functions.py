import csv
import datetime

rows = []
title = ['Категория', 'Наименование', 'Стоимость', 'Дата']


def f_reader():
    global rows
    try:
        with open('Base.csv') as file:
            reader = csv.reader(file, delimiter=',')
            rows = list(reader)
    except IOError:
        print('Ошибка! Файл не найден.')


def add_item():
    item = []
    category = input('Ведите категорию: ')
    item.append(category)
    prod = input('Введите наименование: ')
    item.append(prod)
    price = int(input('Введите цену: '))
    item.append(price)
    while True:
        try:
            date_entry = input('Введите дату в формате ГГГГ-ММ-ДД: ')
            year, month, day = map(int, date_entry.split('-'))
            dt = datetime.date(year, month, day)
        except ValueError:
            print("Некорректный ввод.")
            continue
        else:
            break
    item.append(dt)
    rows.append(item)
    with open('Base.csv', 'w', newline='') as file:
        output = csv.writer(file)
        for row in rows:
            output.writerow(row)


def all_items():
    print('\n{: <10} {: <10} {: <10} {: <10}'.format(*title))
    for row in rows:
        print('{: <10} {: <10} {: <10} {: <10}'.format(*row))


def sort(column):
    param = set()
    for row in rows:
        param.add(row[column])
    tmp = list(param)
    for n, item in enumerate(tmp):
        print(n + 1, item)
    while True:
        try:
            choice = int(input('Для возврата введите 0.\nВведите номер параметра 1-6: '))
        except ValueError:
            print('Ошибка ввода.')
            continue
        if choice in range(1, len(tmp) + 1):
            print('\n{: <10} {: <10} {: <10} {: <10}'.format(*title))
            for row in rows:
                if row[column] == tmp[choice - 1]:
                    print('{: <10} {: <10} {: <10} {: <10}'.format(*row))
            break
        elif choice == 0:
            break
        else:
            print('Ошибка ввода.')


def sort_items():
    rows.sort(key=lambda row: int(row[2]))


def eraser():
    file = open('Base.csv', 'w+')
    file.close()
    f_reader()
    print('\nВсе записи удалены.')
