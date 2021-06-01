# ------- Работа со строками --------

str1 = "This is a string.  "
str2 = "  This is another string."
str3 = "  This is secret string.  "

print(str1 + str2)  # Конкотенация
print(len(str1))  # Длина строки
print(str2.title())  # Первый символ слова в верхнем регистре
print(str1.lower())  # Символы строки в нижнем регистре
print(str2.upper())  # Символы строки в верхнем регистре
print(str1.rstrip())  # Удаление пробелов в конце строки
print(str2.lstrip())  # Удаление пробелов в начале строки
print(str3.strip())  # Удаление пробелов с двух сторон
print(str1.strip("This"))  # Удаление с обоих концов указанные символы

d = "Python"
ch = d[2]  # Извлечение индексированного [] символа 't'. Вывод: Pyhon

# ------- Срезы --------

chm = d[1:3]
print(chm)  # yt
chm = d[1:]
print(chm)  # ython
chm = d[:3]
print(chm)  # Pyt
chm = d[:]
print(chm)  # Python
chm = d[1:5:2]
print(chm)  # yh

# d2 = "Test text"
# d2[2] = 'o'
# print(d2) # TypeError: 'str' object does not support item assignment

# ------- Работа с числами --------

i = 10
j = 5

print(i / j)  # 2.0
print(i % j)  # 0
print(i ** j)  # 100000

# param = str3 + 15 # TypeError: can only concatenate str (not "int") to str

# ------- Преобразование данных --------

param = str3 + str(15)
print(param)

n1 = input("Введите первое число: ")
n2 = input("Введите второе число: ")
n3 = float(n1) + float(n2)
print("Результат: " + n1 + " + " + n2 + " = ", n3)

# ------- Форматирование строк ------

a = 1 / 3
print("{:7.3f}".format(a))
a = 2 / 3
b = 2 / 9
print("{:7.3f} {:7.3f}".format(a, b))
print("{:10.3e} {:10.3e}".format(a, b))

n1 = input("Введите первое число: ")
n2 = input("Введите второе число: ")
n3 = float(n1) + float(n2)
str4 = f"""{n1} + {n2} = {n3}"""
print("Результат: ", str4)

# ------------- Списки ------------

list1 = [82, 8, 23, 97, 92, 44, 17, 39, 11, 12]

print(dir(list1))

help(list1.insert)
help(list1.append)
help(list1.sort)
help(list1.remove)
help(list1.reverse)

list1[0] = 1
list1[1] = 2
print(list1)

list1.append(999)
print(list1)

list1.insert(4, 10)
print(list1)

list1.remove(list1[0])
print(list1)

list1.remove(list1[-1])
print(list1)

# ------------- Сортировка элементов списка ------------

list1.sort(reverse=True)
print('Отсортированный список: ', list1)

sorted(list1, reverse=True)
print(list1)

list2 = [3, 5, 6, 2, 33, 6, 11]
lis = sorted(list2)
print("Список: ", list2)
print("Отсортированнный список: ", lis)

# ------- Кортежи -------

print(dir(tuple))

help(tuple.index)
help(tuple.count)

seq = (2, 8, 23, 97, 92, 44, 17, 39, 11, 12)
print(seq)

print(seq.count(8))
print(seq.index(44))

listseq = list(seq)

print(type(listseq))

listseq.append(999)
print(listseq)

listseq.insert(2, 3)
print(listseq)

listseq.remove(listseq[-1])
print(listseq)

# -------- Словари ---------

D = {"food": "Apple", "quantity": 4, "color": "Red"}

D["food"]
D["quantity"] += 10

n = input("Введите имя: ")
a = input("Введите возраст: ")
dct = {n: a}
print(dct)

#------- Вложенность хранения данных --------

rec = {"name": {"firstname": "Bob", "lastname": "Smith"},
       "job": ["dev", "mgr"],
       "age": 25}

print(rec["name"])
print(rec["name"]["firstname"])
print(rec["job"])
rec["job"].append("janitor")
print(rec)

