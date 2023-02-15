import random as r
import re

# kop = int(input("Введите число от 1 до 99: "))
# if 1 <= kop <= 99:
#     if kop % 10 == 1 and kop != 11:
#         print(kop, "копейка")
#     elif kop % 10 == 3 and kop != 13:
#         print(kop, "копейки")
#     elif kop % 10 == 2 and kop != 12:
#         print(kop, "копейки")
#     elif kop % 10 == 4 and kop != 14:
#         print(kop, "копейки")
#     else:
#         print(kop, "копеек")
# else:
#     print("Слишком много копеек, сам считай")


# DZ 14/12/22

# dz 1
# a = int(input("Количество символов: "))
# b = input("Тип символа: ")
# c = int(input("Ориентация линии (напиши 0 или 1): "))
# while a > 0:
#     print(b, end="")
#     a -= 1
#     if c == 1:
#         print("")
#     else:
#         end=""


# унарный минус умножить на -1

# dz 2 я не понимаю, откуда он берет шестую строку!!!

# c = 5
# d = 0
# while d < c:
#     if d % 2 == 0:
#         print("+" * 16, "\n", end="")
#     if d % 2 == 0:
#         print("-" * 16, "\n", end="")
#     d += 1

# dz 3
#
# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# c = int(input("Введите третье число: "))
# maxi = a if a > b else c
# print(maxi)

# dz 4

# a = int(input("Выберите первое число: "))
# b = int(input("Выберите второе число: "))
# c = input("Введите оператор (+,-,/,*,**,%,r,<,>):")
# result = 0
# if c == "+":
#     result = a + b
# elif c == "-":
#     result = a - b
# elif c == "*":
#     result = a * b
# elif c == "**":
#     result = a ** b
# elif c == "r":
#     result = a * -1 # ? а что делать с b ?
# if b != 0:
#     if c == "/":
#         result = a / b
#     elif c == "%":
#         result = a % b
#     elif b == 0:
#         result = "Делить на 0 нельзя"
# print("Результат: ", result)

#  запуталась, как сделать > и < , не получилось...


# ---------------- DZ 15.12.22 ----------------

# ---------------- DZ 1 ----------------
#
# a = [int(input("Введите элемент списка: ")) for i in range(int(input("Введите длину списка: ")))]
# s = []
# print("Список: ", a)
# for i in range(len(a)):
#     if a[i] > 0:
#         s.append(a[i])
# print("Новый список, состоящий из положительных элементов: ", s)
# b = max(a)
# print("Наибольший элемент списка: ", b)


# ---------------- DZ 2 -----------------

# n = [int(input("-> ")) for i in range(int(input("n = ")))]
# k = int(input("Введите индекс: "))
# c = int(input("Введите значение: "))
# n.remove(n[k])
# n.insert(k, c)
# print(n)


# ---------------- DZ 3 ---------------

# i = 1
# while i < 11:
#     print(i**2, end=" ")
#     i += 1
#    не разобралась, как append-ом сделать!

# ------------------ DZ 19.12.22 ----------

# ------------- DZ 1 --------------

# a = [int(input("--> ")) for i in range(int(input("n = ")))]
# b = int(input("Введите число: "))
# for i in a:
#     if b in a:
#         print("Число присутствует в элементах списка")
#         break

# ------------- DZ 2 --------------


# a = [r.randint(0,100) for i in range(20)]
# print(a)
# print("Summa: ", sum(a))

# ------------ DZ 3 ---------------

# a = [r.randint(0,100) for i in range(10)]
# maxi = max(a)
# a.sort(reverse=True)
# print(maxi)
# print(a)

# -------------- DZ 4 --------------
# w, h = 3, 4
# m = [[r.randint(0, 4) for x in range(w)] for y in range(h)]
# pr = 1
# for h in m:
#     for w in h:
#         print(w, end="\t\t")
#         if w > 0:
#             pr *= w
#     print()
# print(pr)


# ----------- DZ 5 ------------
#
# n = int(input("Размерность матрицы: "))
# mas = []
# for i in range(n):
#     mas.append([])
#     for j in range(n):
#         mas[i].append(r.randint(1, 100))
# print(mas)
# for row in mas:
#     for x in row:
#         print(x, end="\t")
#     print()
# print()
# m = 101
# lst = []
# for k in range(n):
#     if m > mas[k][k]:
#         lst.append(mas[k][k])
# print(lst, end="\t")
# print("\n", min(lst))


# ----------- DZ 6 ------------
#
# w, h = 3, 4
# m = [[r.randint(-20, 10) for x in range(w)] for y in range(h)]
# kol = []
# for h in m:
#     for w in h:
#         print(w, end="\t\t")
#         if w < 0:
#             kol.append(w)
#             m.count(w)
#     print()
# print("Количество отрицательных элементов: ", kol) # количество count-ом надо сделать? почему-то не получилось!:(

# ---------------- DZ 20/12/22 -------------
#
# import math
#
# fig = input("Выберите фигуру (1 - прямоугольник, 2 - треугольник, 3 - круг): ")
# if fig == "1":
#     a = float(input("Введите сторону a: "))
#     b = float(input("Введите сторону b: "))
#     c = float(input("Введите сторону c: "))
#     p = int(a + b + c) / 2
#     v = math.sqrt((p * (p - a) * (p - b) * (p - c)))
# elif fig == "2":
#     a = float(input("Введите сторону a: "))
#     b = float(input("Введите сторону b: "))
#     v = a * b
# elif fig == "3":
#     r = float(input("Введите радиус: "))
#     v = math.pi*(r**2)
# print("Площадь: ", v)


# ------------ DZ 22.12.22 -----------

# tpl = (2, 5, 3, 5, 2, 3, 6, 5, 1)
# print(tpl)
# a = tpl.count(2)
# print("Количество 2 = ", a)
# b = tpl.count(5)
# print("Количество 5 = ", b)
# c = tpl.count(3)
# print("Количество 3 = ", c)
# d = tpl.count(6)
# print("Количество 6 = ", d)
# e = tpl.count(1)
# print("Количество 1 = ", e)

# --------------------------------------
# lst1 = [1, 2, 3, 3, 2]
# lst2 = [2, 1, 3, 1, 2, 5, 5, 9, 2, 0, 0]
#
#
# def lst_reverse(lst):
#     # lst.reverse()
#     unique = []
#     for i in lst[::-1]:
#         if i not in unique:
#             unique.append(i)
#         return tuple(unique)
#
#
# print(lst_reverse(lst1))
# print(lst_reverse(lst2))

# --------------------------------------

# tpl = ('ab', 'abcd', 'cde', 'abc', 'def')
# s = input("s => ")
# for i in tpl:
#     if s in tpl:
#         print("Yes")
#         break
#     else:
#         print("No")
#

# -------------DZ 28.12.22---------------------------------------

# a = "Python"
# b = "Programming Language"
# s = set(a) - set(b)
# print(s)

# ------------------------------------

# a = "Привет мир!"
# b = "а,и,о,у,ы,э,е,ё,ю,я"
# s = set(a) & set(b)
# print(s)

# ------------------------------------

# a = "test"
# b = "string"
# s = set(a) | set(b)
# print(s)

# -------------------------------------

# a = "hello"
# b = "world"
# s = set(a) ^ set(b)
# print(s)


# ----------------- DZ 4/01/23 ---------------------------------------------------------------------------------------

# a = ('red', 'green', 'blue')
# b = ('#FF0000', '#008000', '#0000FF')
# dict = dict(zip(a, b))
# print(dict)

# -----------------------------------------------

# dict = {a: a ** 3 for a in range(1, 11)}
# print(dict)

#  ----------------------------------------------

# a = {1: 10, 2: 20}
# b = {3: 30, 4: 40}
# c = {5: 50, 6: 60}
# d = a | b | c
# print(d)

# ----------------------------------------------

# all = {
#     "emp1": {"name": 'John', "salary": 7500},
#     "emp2": {"name": 'Emma', "salary": 8000},
#     "emp3": {"name": 'Brad', "salary": 6500},
# }
# new_salary = 8500
# (all["emp3"]["salary"]) = new_salary
#
# for x in all:
#     print(x)
#     for y in all[x]:
#         print("\t", y, ": ", all[x][y], sep="")

#  ---------------------------------------------
#
# names = []
# scores = []
# for i in range(int(input("Количество студентов: "))):
#     name = input("1й студент: ")
#     score = int(input("Балл: "))
#     names.append(name)
#     scores.append(score)
#
# middle_score = sum(scores) / len(scores)
# print("Средний балл: ", middle_score)
#


# stud_up = 0
# for s in scores:
#     if middle_score >= ????:
#         print("Студенты с баллом выше среднего: ")
#         s += 1
# -------
# stud = {}
# n = int(input("Количество студентов: "))
# s = 0
# for i in range(n):
#     sname = input(str(i+1) + "- й студент: ")
#     point = int(input("Балл: "))
#     stud[sname] = point
#     s += point
#
# avrg = s/n
# print(stud)
# print(round(avrg, 2))
#
# for i in stud:
#     if stud[i] > avrg:
#         print(i)

#  ----------------------------------------
# a = ('color', 'fruit', 'pet')
# b = ('blue', 'apple', 'dog')
# new_dict = dict(zip(a, b))
# print(new_dict)

# ---------------------- DZ 10/01/23 -------------------------------------
# a = 0
# b = 0
# c = 0
#
#
# def square(x, y, z):
#     global a, b, c
#     return 2 * (x * y + y * z + x * z)
#
#     # def inner():
#     #     return a * b
#     # return inner()
#
#
# print(square(2, 4, 6))
# print(square(5, 8, 2))
# print(square(1, 6, 8))

# --------------------------DZ 12/01/23 ---------------------------------------
# print((lambda a: a * 2)(15))
# print((lambda a: a * 2)(20))
#
# print((lambda a: a * 3)(15))
# print((lambda a: a * 3)(20))


# ---------------- 2 ----------------

# print((lambda n, x, d: n * x * d)(2, 5, 5))

# ----------------- 3 ---------------------

# stud = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nicolas', 'final': 98}
# ]
#
# sort = sorted(stud, key=lambda item: item['name'])
# print(sort)
# sort = sorted(stud, key=lambda item: item['final'], reverse=True)
# print(sort)

# ---------------- 4 ------------------------
#
# stud = [
#     {'name': 'Jennifer', 'final': 95},
#     {'name': 'David', 'final': 92},
#     {'name': 'Nicolas', 'final': 98}
# ]
# maxi = sorted(stud, key=lambda item: item['final'], reverse=True)
# print(maxi[0])
# mini = sorted(stud, key=lambda item: item['final'])
# print(mini[0])


# ---------------------DZ 18/01/23-------------------------------------------
#
# def decor(args1, args2):
#     def args_dec(fn):
#         def wrap(w, x, y, z):
#             print(args1, w, args2, x, args2, y, args2, z, "=", end=' ')
#             fn(w, x, y, z)
#
#         return wrap
#     return args_dec
#
#
# @decor("Сумма чисел", ",")
# def summa(a, b, c, d):
#     print(a + b + c + d)
#
#
# @decor("Среднее арифметическое чисел", ",")
# def score(a, b, c, d):
#     print((a + b + c + d) / 4)
#
#
# summa(2, 3, 3, 4)
# score(2, 3, 3, 4)

# -----------------------DZ 23/01/23 ------------------------------------------------------

# str1 = "Я изучаю Nython. Мне нравится Nython. Nython очень интересный язык программирования."
# str2 = " "
# for i, x in enumerate(str1):
#     if i % 2 == 0:
#         str2 += '@'
#     else:
#         str2 += x
# print(str2)

# -----------------------------------------------------------------
#
# s = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# index = int(input("Введите число от 0 до 9: "))
# s2 = s[:index] + s[index+1:]
# print(s2)

# ----------------------------------------------------------------
# s = [0, 1, 2, 3, 4, 5, 3, 6, 3, 7, 3, 8, 4, 9, 4]
# index = int(input("Введите число от 0 до 9: "))
# s.remove(index)
# print(s)
#

# # ---------------------------------------------------------------
# s = "0, 1, 2, 3, 4, 5, 3, 6, 3, 7, 3, 8, 4, 9, 4"
#
# del_s = input("Введите число от 0 до 9: ")
#
# s2 = s.replace(del_s, '')
#
#
# print(s)
# print(s2)
# ---------------------------------------------------------------
# x = int(input("Введите число: "))
# y = ""
#
# while x > 0:
#     a = str(x % 2)
#     y = a + y
#     x = int(x / 2)
#
# print(y)
# -----------------------DZ 26/01/23-----------------------------------------

# s = "I am learning Python, hello, WORLD!"
# x = s.find('h')
# y = s.rfind('h')
# res = s[0:x] + s[y + 1:]
# print(res)

# ----------------------------------------------------------------------------

# s = "I am learning Python, hello, WORLD!"
# x = s.find('h')
# y = s.rfind('h')
#
# h1 = s[0:x]
# h2 = s[y + 1:]
# res = h1 + h2
# res2 = s[h1:0] + s[h2:0]
# print(res)
# print(res2)
# ....

# -------------------------------------------------------------------------------

# s = "11, 23, 44, 55, 23, 22"
# change = input("Ее заменяемая подстрока: ")
# new = input("Новая подстрока: ")
# print(s)
# print(s.replace(change, new))

# ------------------------------------------------------------------------------
#
# s = """Ежевику для ежат
# Принесли два ежа.
# Ежевику  еле-еле
# Ежата возле ели съели"""
# print(s)
# print("Количество слов: ", s.count(' е') + s.count(' Е'))
# r'[A-z\.]+[-@_+]{6,18}'
# ------------------------------ DZ 01/02/23 ----------------------------------
import re
#
#
# def validate_name(name):
#
#     return re.findall(r'^[a-z\d@_-]{6,18}$', name, re.IGNORECASE)
#
#
# print(validate_name('my-p@ssw0rd'))

# ------------------------------------------------------------------
# test = "В июне 2021 года, 02/06/2021, 05/06/2021, 14/06/2021, были зафиксированы максимумы ежемесячных осадков."
# r1 = '[0-2][0-9]/[0-2][0-9]/20[0-2][0-2]'
# print(re.findall(r1, test))

# ----------------------------- DZ 06/02/23 -------------------------------------
# ----------------------------1 ый способ мой------------------------------------------
# import re
# s = '+7 499 456-45-78, +74994564578, 7 (499) 456 45 78, 7 (499) 456-45-78'
# reg = r'[+]?7+\s?[(]?[\d{3}]+[)]?\s?[-]?[\d{3}]+\s?[-]?[\d{2}]+\s?[-]?[\d{2}]+'
# print(re.findall(reg, s))
# ---------------------------------2ой способ--------------------------------------------------
# def validate_phone(number):
#     reg = r"^\+?7\s*\(?\d{3}\)?\s*[\d\s-]{7,9}$"
#     #return re.search(reg, number).group()
#     return re.findall(reg, number)[0]
#
#
# print(validate_phone('+7 499 456-45-78'))
# print(validate_phone('+74994564578'))
# print(validate_phone('7 (499) 456 45 78'))
# print(validate_phone('7 (499) 456-45-78'))
# -------------------------------------------------------------------------------

# def negative(a):
#     if len(a) == 0: # a == [] # if not a  3 варианта
#         return 0
#     else:
#         count = negative(a[1:])
#         if a[0] < 0:
#             count += 1
#         return count
#
#
# lst = [-2, 3, 8, -11, -4, 6]
# print(lst)
# n = negative(lst)
# print(n)

# -------------------------------DZ 07/02/23-------------------------------------------

from random import randint

#
#
# def binary_search(s, item):
#     found = False
#     first = 1
#     last = len(s) - 1
#     while first <= last and not found:
#         midpoint = (first + last) // 2
#         if s[midpoint] == item:
#             found = True
#         else:
#             if item < s[midpoint]:
#                 last = midpoint - 1
#             else:
#                 first = midpoint + 1
#
#     return found
#
#
# a = [randint(1, 100) for i in range(10)]
# print(a)
# a.sort()
# print(a)
# n = int(input("Введите число: "))
# if binary_search(a, n):
#     print(f"Число {n} в списке присутствует")
# else:
#     print(f"Число {n} в списке отсутствует")

# --------------------------- DZ 13/02/23 ------------------------------

# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# if c:
#     print(f"Число {b} в списке присутствует")
# else:
#     print(f"Число {b} в списке отсутствует")
#
# a = [randint(1, 10) for i in range(10)]
# b = int(input("Введите число:"))
# print(a)
# c = seq_search(a, b)

# ---------------------------------------------------------------------

# test = ["Замена строки в текстовом файле",
#         "Изменить строку в списке",
#         "Записать список в файл"]
#
# pos = 1
# print(test)
# test.pop(pos)
# print(test)

# ---------------------------------------------------------------------
# a = [5, 9, 6, 7]
# b = [3, 11, 8]
# c = [2, 4]
# d = [10, 1, 12]
# abcd = a+b+c+d
#
#
# def seq_search(s, item):
#     pos = 0
#     found = False
#     while pos < len(s) and not found:
#         if s[pos] == item:
#             found = True
#         else:
#             pos += 1
#     return found
#
#
# sort = int(input("1 or 2: "))
# if sort == 1:
#     abcd.sort(reverse=True)
# else:
#     abcd.sort()
#
# print(abcd)
# poisk = int(input("Введите значение для поиска: "))
# searching = seq_search(abcd, poisk)
# if poisk in abcd:
#     print(f"Значение {poisk} найдено")
# else:
#     print(f"Значение {poisk} не найдено")

# ---------------------------- DZ 15/02/23 -----------------------------

# import os
#
# # print(open(r"D:\Study\PYTHON\new\Work\f3.txt", "w").write(
# #   open(r"D:\Study\PYTHON\new\Work\file1.txt", "r").read() + open(r"D:\Study\PYTHON\new\Work\file2.txt", "r").read()))
#
# one_file = 'file1.txt' # запись из одного файла в другой
# two_file = 'file2.txt'
# with open(read_file, 'r') as fr, open(write_file, 'w') as fw:
#     for line in fr:
#         line = line.replace("Строка", "Линия - ")
#         fw.write(line)
# -----------------------------------------------------------------------
# file_name = "test.txt"
#
#
# def is_exist(fl):
#     if os.path.exists(fl):
#         print("hello")
#     else:
#         print("kl;d")
#
#
# # print(os.getcwd()) # возвращает путь к текущей директории
# # print(os.path.basename(r'D:\Study\PYTHON\new\test\test2.txt'))  # имя директории
# # print(os.path.getatime(path)) # время последнего доступа к файлу
# f = open(file_name, 'w')
# print(f.write('helo'))
# f.close()
#
