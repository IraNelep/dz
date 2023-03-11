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

import os


# a = r"D:\Study\PYTHON\new\Work\f3.txt"
# b = r"D:\Study\PYTHON\new\Work\file1.txt"
# c = r"D:\Study\PYTHON\new\Work\file2.txt"
# open(a, "w").write(open(b, "r").read() + open(c, "r").read())


# -----------------------------------------------------------------------

# file_path = r'D:\Study\PYTHON\new\test.txt'
# if os.path.exists(file_path):
#     dirs, name = os.path.split(file_path)
#     atime = os.path.getatime(file_path)
#     print(f"{name} ({dirs}) - last access time {atime} seconds")
# else:
#     print(f"Файл {file_path} не существует")

# ---------------------------DZ19/02/23------------------------------------
# class Rectangle:
#     length = 3
#     width = 9
#     # square = 0
#     # per = 0
#     # gip = 0
#
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#         print("Длина прямоугольника:", self.length)
#         print("Ширина прямоугольника:", self.width)
#         # self.square = square
#         # self.per = per
#         # self.gip = gip
#
#     def get_square(self):
#         print("Площадь прямоугольника:", self.length * self.width)
#         print("Периметр прямоугольника:", self.length + self.width + self.length + self.width)
#         print("Гипотенуза прямоугольника:", ((self.length ** 2) + (self.width ** 2)) ** 0.5)
#
#     def stars(self):
#         for i in range(self.length):
#             print("*" * self.width)
#
#
# r1 = Rectangle(3, 9)
# r1.get_square()
# r1.stars()

# -------------------------- DZ 27/02/23 --------------------------------
# import math
#
#
# class Sphere:
#
#     def __init__(self, pi, radius, a, b, c):
#         self.pi = pi
#         self.radius = radius
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @staticmethod
#     def get_radius(radius):
#         print("get_radius:", radius)
#
#     @staticmethod
#     def get_volume(a, b):
#         print("get_volume:", (4 / 3) * a * (b ** 3))
#
#     @staticmethod
#     def get_square(a, b):
#         print("get_square:", 4 * a * (b**2))
#
#     @staticmethod
#     def get_center(a, b, c):
#         print("get_center:", (a, b, c))
#
#     def set_radius(self, new_radius):
#         self.radius = new_radius
#         print(f"set_radius({new_radius}): {new_radius}")
#
#     def is_point_inside(self, x, y, z):
#         self.a = x
#         self.b = y
#         self.c = z
#         if math.sqrt((x ** 2) + (y ** 2) + (z ** 2)) <= self.radius:
#             print(f"is_point_inside({x}, {y}, {z}): ", True)
#         else:
#             print(f"is_point_inside({x}, {y}, {z}): ", False)
#
#
# s1 = Sphere(3.14, 0.6, 0, 0, 0)
# Sphere.get_radius(0.6)
# Sphere.get_volume(3.14, 0.6)
# Sphere.get_square(3.14, 0.6)
# Sphere.get_center(0, 0, 0)
# Sphere.get_square(3.14, 0.6)
# s1.is_point_inside(0, -1.5, 0)
# s1.set_radius(1.6)
# s1.is_point_inside(0, -1.5, 0)
# ---------------------------------2 способ
# from math import pi
#
#
# class Sphere:
#     def __init__(self, radius=1.0, x=0, y=0, z=0):
#         self.radius = radius
#         self.x = x
#         self.y = y
#         self.z = z
#
#     def get_radius(self):
#         return self.radius
#
#     def set_radius(self, ra):
#         self.radius = ra
#
#     def get_volume(self):
#         return 4 / 3 * (pi * self.radius ** 3)
#
#     def get_square(self):
#         return 4 * pi * self.radius ** 2
#
#     def get_center(self):
#         return self.x, self.y, self.z
#
#     def is_point_inside(self, x, y, z):
#         if ((self.x - x) ** 2 + (self.y - y) ** 2 + (self.z - z) ** 2) <= self.radius ** 2:
#             return True
#         else:
#             return False
#
#
# s = Sphere(0.6)
# print("get_radius:", s.get_radius())
# print("get_volume:", s.get_volume())
# print("get_square:", s.get_square())
# print("get_center:", s.get_center())
# print("is_point_inside:", s.is_point_inside(0, -1.5, 0))
# print("set_radius:", s.set_radius(1.6))
# print("is_point_inside:", s.is_point_inside(0, -1.5, 0))


# -------------------------- DZ 01/03/23 ----------------------------------------


# class Account:
#     rate_usd = 0.013
#     rate_eur = 0.011
#     suffix = "RUB"
#     suffix_usd = "USD"
#     suffix_eur = "EUR"
#
#     def __init__(self, surname, num, percent, value=0):
#         self.num = num
#         self.__surname = surname  # new
#         self.__percent = percent
#         self.__value = value
#         print(f"Счет №{self.num} принадлежащий {self.__surname} был открыт.")
#         print("*" * 50)
#
#     def __del__(self):
#         print("*" * 50)
#         print(f"Счет №{self.num} принадлежащий {self.__surname} был закрыт.")
#
#     def get_surname(self):  # get surname
#         return self.surname
#
#     def set_surname(self, surname):  # set surname
#         self.__surname = surname
#
#     @property  # property surname
#     def surname(self):
#         return self.__surname
#
#     @surname.setter  # property surname
#     def surname(self, surname):
#         self.__surname = surname
#
#     @staticmethod
#     def convert(value, rate):
#         return value * rate
#
#     def get_value(self):  # get value
#         return self.value
#
#     def set_value(self, value):  # set value
#         self.__value = value
#
#     @property # property value
#     def value(self):
#         return self.__value
#
#     @value.setter # property value
#     def value(self, value):
#         self.__value = value
#
#     @classmethod
#     def set_usd_rate(cls, rate):
#         cls.rate_usd = rate
#
#     @classmethod
#     def set_eur_rate(cls, rate):
#         cls.rate_eur = rate
#
#     def print_balance(self):
#         print(f"Текущий баланс {self.__value} {Account.suffix}")
#
#     def convert_to_usd(self):
#         usd_val = Account.convert(self.__value, Account.rate_usd)
#         print(f"Состояние счета: {usd_val} {Account.suffix_usd}")
#
#     def convert_to_eur(self):
#         usd_eur = Account.convert(self.__value, Account.rate_eur)
#         print(f"Состояние счета: {usd_eur} {Account.suffix_eur}")
#
#     def edit_owner(self, surname):
#         self.__surname = surname
#
#     def get_percent(self):  # get percent
#         return self.percent
#
#     def set_percent(self, percent):  # set percent
#         self.__percent = percent
#
#     @property  # property percent
#     def percent(self):
#         return self.__percent
#
#     @percent.setter  # property percent
#     def percent(self, percent):
#         self.__percent = percent
#
#     def add_percents(self):
#         self.__value += self.__value * self.__percent
#         print("Проценты были успешно начислены!")
#         self.print_balance()
#
#     def withdraw_money(self, val):
#         if val > self.__value:
#             print(f"К сожалению, у вас нет {val} {Account.suffix}")
#         else:
#             self.__value -= val
#             print(f"{val} {Account.suffix} было успешно снято!")
#         self.print_balance()
#
#     def add_money(self, val):
#         self.__value += val
#         print(f"{val} {Account.suffix} было успешно добавлено!")
#         self.print_balance()
#
#     def print_info(self):
#         print("Информация о счете:")
#         print("-" * 20)
#         print(f"№ {self.num}")
#         print(f"Владелец: {self.__surname}")
#         self.print_balance()
#         print(f"Проценты: {self.__percent:.0%}")
#         print("-" * 20)
#
#
# acc = Account(num='12345', surname="Долгих", percent=0.03, value=1000)
# acc.print_info()
# acc.convert_to_usd()
# acc.convert_to_eur()
# print()
# Account.set_usd_rate(2)
# acc.convert_to_usd()
# Account.set_eur_rate(3)
# acc.convert_to_eur()
# acc.convert_to_eur = '46' # property value
# acc.convert_to_usd = '56' # property value
# print()
# acc.edit_owner("Дюма")
# acc.surname = "Дюма"  # property surname
# acc.print_info()
# print()
# acc.add_percents()
# acc.percent = '76'  # property percent
# print()
# acc.withdraw_money(100)
# print()
# acc.withdraw_money(3000)
# print()
# acc.add_money(5000)
# print()


# ----------------------------- DZ 04/03/23 ------------------------------------
# from math import sqrt
#
#
# class Pair:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     @property  # property a
#     def a_change(self):
#         return self.a
#
#     @a_change.setter  # property a
#     def a_change(self, a):
#         self.a = a
#
#     @property  # property b
#     def b_change(self):
#         return self.b
#
#     @b_change.setter  # property b
#     def b_change(self, b):
#         self.b = b
#
#     def pro(self):
#         print("Произведение:", self.a * self.b)
#
#     def summa(self):
#         print("Сумма:", self.a + self.b)
#
#
# class RightTriangle(Pair):
#
#     def hyp(self):
#         hyp = round(sqrt(self.a**2 + self.b**2), 2)
#         print("Гипотенуза ABC:", hyp)
#
#     def square(self):
#         print("Площадь ABC:", float((self.a * self.b) // 2))
#
#     def print_info(self): # я не поняла, как сюда передать гипотенузу...
#         print("Прямоугольный треугольник ABC:", self.a, self.b)
#
#
# r1 = RightTriangle(5, 8)
# r1.hyp()
# r1.print_info()
# r1.square()
# print()
# p = Pair(5, 8) # pair
# p.summa()
# p.pro()
# print()
# r1.a_change = 10 # property a
# r1.b_change = 7 # property b
# r1.hyp()
# r1.a_change = 10
# r1.b_change = 20
# r1.hyp()
# r1.summa()
# r1.pro()
# r1.square()

# ------------------------------ DZ 07/03/23 -----------------------------
# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.lp = self.Laptop()
#
#     def show(self):
#         print(f'{self.name} =>')
#
#     class Laptop:
#         def __init__(self, mod='HP', pro=17, memory=16):
#             self.mod = mod
#             self.pro = pro
#             self.memory = memory
#
#         def display(self):
#             print(f'{self.mod}, {self.pro}, {self.memory}')
#
#
# stud1 = Student('Roman')
# stud1.show()
# g = stud1.lp
# g.display()
# print()
# stud2 = Student('Vladimir')
# stud2.show()
# g = stud2.lp
# g.display()


# ------------------------------ второй способ

# class Student:
#     def __init__(self, name):
#         self.name = name
#         self.note = self.Notebook()
#
#     def show(self):
#         print(self.name, end=' ')
#         self.note.show()
#
#     class Notebook:
#         def __init__(self):
#             self.brand = 'HP'
#             self.cpu = 'i7'
#             self.ram = 16
#
#         def show(self):
#             print(f'=> {self.brand}, {self.cpu}, {self.ram}')
#
#
# s1 = Student("Roman")
# s2 = Student("Vladimir")
#
# s1.show()
# s2.show()

# ------------------------------ DZ 11.03.23 --------------------------------

class Clock:
    __DAY = 86400

    def __init__(self, sec: int):
        if not isinstance(sec, int):
            raise ValueError("Секунды должны быть целым числом")
        self.sec = sec % self.__DAY


    def get_format_time(self):
        s = self.sec % 60
        m = (self.sec // 60) % 60
        h = (self.sec // 3600) % 24
        return f"{Clock.__get_form(h)}:{Clock.__get_form(m)}:{Clock.__get_form(s)}"

    @staticmethod
    def __get_form(x): # добавили первый ноль
        return str(x) if x > 9 else "0" + str(x)

    def __add__(self, other): # сложение
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __sub__(self, other): # вычитание
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __mul__(self, other):  # умножение
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __floordiv__(self, other): # деление
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)

    def __mod__(self, other): # остаток от деления
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типом Clock")
        return Clock(self.sec + other.sec)


c1 = Clock(100)
c2 = Clock(200)
c1 += c2
c1 -= c2
c1 *= c2
c1 //= c2
c1 %= c2

print(c1.get_format_time())
# print(c2.get_format_time())
