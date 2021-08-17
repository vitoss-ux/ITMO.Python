import Functions as func


def start_menu():
    print('Привет %UserName')

    print("1. Добавить запись")
    print("2. Показать всё")
    print("3. Сортировать по дате")
    print("4. Сортировать по категории")
    print("5. Сортировать по цене min->max")
    print("6. Удалить")
    print("0. Выход")

    while True:
        try:
            button = int(input('Введи команду: '))
        except ValueError:
            print('Упс! Неверная команда...')
            continue
        if button == 1:
            print('Добавление записи...')
            func.add_item()
        if button == 2:
            print('Все записи...')
            func.all_items()
        if button == 3:
            print('Отсортировано по дате:')
            func.sort(3)
        if button == 4:
            print('Отсортировано по категории:')
            func.sort(0)
        if button == 5:
            print('Отсортировано по цене min->max:')
            func.sort_items()
            func.all_items()
        if button == 6:
            print('Все записи удалены!')
            func.eraser()
        if button == 0:
            print('Выход.')
        else:
            print('Упс! Неверная команда...')
