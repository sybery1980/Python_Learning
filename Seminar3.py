# Задача 17
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


#n = int(input('Введите  длину списка: '))

# b = [1, 1, 2, 0, -1, 3, 4, 4]
# a = set(b)
# print(b)
# print(a)
# print(len(a))


# Задача 19
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический)
# на K элементов вправо,  K – положительное число.


                         # Вариант 1

# Input:   [1, 2, 3, 4, 5] k = 2
# Output:  [4, 5, 1, 2, 3]

# K = 2
# m = [1, 2, 3, 4, 5]
# result = []
# for i in range(0, K):
#     m.insert(0, m[-1])
#     m.pop(-1)
#     print(m)
   
   
   
                          # Вариант 2
    
# import random

# n = int(input('Введите длину списка >>> '))
# l = []
# for num in range(0,n):
    
#     random_number = round(random.randint(-10,10))
#     l.append(random_number)
# print(l)

# k = int(input('Введите на сколько индексов сдвигать >>> '))
# for i in range(k):
#     p = l.pop(-1)
#     l.insert(0, p)

# print(l)





                                        # Задача 23

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# 23
# Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива,
# больших предыдущего (элемента с предыдущим номером) 

# Input: [0, -1, 5, 2, 3]
# Output: 2 
# пояснение
# (-1 < 5, 2 < 3)

# array = [0, -1, 5 ,2 ,3, 3, 9, 7, 6, 9]
# count = 0
# for i in range(0, len(array)-1):
#     if array[i] < array[i+1]:
#         count += 1
        
#         print(array)
#         print(count)
        
#         print('\n\n\n')
        
        
        
        # Напишите программу для печати всех уникальных значений в словаре. 

# Input:  
# inpDict = {"I": "S001","II": "S002", "IV": "S005","V": " S005 ","VI": " S009 ","VII": " S007 ",}

# inpDict = {"I": "S001","II": "S002", "IV": "S005","V": " S005 ","VI": " S009 ","VII": " S007 ",}

# res = set(inpDict.values())

# print(inpDict.values(),"\n")
# print(sorted(res))



# Задача 20: домашняя работа
# В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка;
# B, C, M, P – 3 очка;
# F, H, V, W, Y – 4 очка;
# K – 5 очков;
# J, X – 8 очков;
# Q, Z – 10 очков.

# А русские буквы оцениваются так:
# А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# Д, К, Л, М, П, У – 2 очка;
# Б, Г, Ё, Ь, Я – 3 очка;
# Й, Ы – 4 очка;
# Ж, З, Х, Ц, Ч – 5 очков;
# Ш, Э, Ю – 8 очков;
# Ф, Щ, Ъ – 10 очков.

# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.

# Ввод: ноутбук
# Вывод: 12

# # Вариант 1
# points_en = {1: 'AEIOULNSTR', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JZ', 10: 'QZ'}
# points_ru = {1: 'АВЕИНОРСТ', 2: 'ДКЛМПУ', 3: 'БГЁЬЯ', 4: 'ЙЫ', 5: 'ЖЗХЦЧ', 8: 'ШЭЮ', 10: 'ФЩЪ'}
# word = input().upper()  # переводим все буквы в верхний регистр
# count = 0
# for i in word:
#     if i in 'QWERTYUIOPASDFGHJKLZXCVBNM':
#         for j in points_en:
#             if i in points_en[j]:
#                 count = count + j
#     else:
#         for j in points_en:
#             if i in points_ru[j]:
#                 count = count + j
# print(count)

# Вариант 2
# dictionary = {
# 'a':1, 'e':1, 'i':1, 'l':1, 'n':1, 'o':1, 'r':1, 's':1, 't':1, 'u':1,
# 'd':2, 'g':2,
# 'b':3, 'c':3, 'm':3, 'p':3,
# 'f':4, 'h':4, 'v':4, 'w':4, 'y':4,
# 'k':5,
# 'j':8, 'x':8,
# 'q':10, 'z':10,
# 'а':1, 'в':1, 'е':1, 'и':1, 'н':1, 'о':1, 'р':1, 'с':1, 'т':1,
# 'д':2, 'к':2, 'л':2, 'м':2, 'п':2, 'у':2,
# 'б':3, 'г':3, 'ё':3, 'ь':3, 'я':3,
# 'й':4, 'ы':4,
# 'ж':5, 'з':5, 'х':5, 'ц':5, 'ч':5,
# 'ш':8, 'э':8, 'ю':8,
# 'ф':10, 'щ':10, 'ъ':10
# }

# word = input('Введите слово -> ')
# word = word.lower()

# result = 0
# for i in word:
#     result += dictionary[i]

# print('Стоимость введенного вами слова:', result)



# Задача 18:
# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N.
# Выведите, ближайший к X элемент. Если есть несколько элементов, которые равноудалены от X, выведите наименьший по величине.

# Ввод: 10
# Ввод: 7
# 1 2 1 8 9 6 5 4 3 4
# Вывод: 6


# N = int(input('Введите массива:' ))
# a = [int(input('Ввести число:')) for i in range(N)]
# x = int(input('Заданное число:'))

# minraz =(x — a[0])**2 # Минимальная разница по модулю (для сравнения первый элемент)

# b = 0 # Нулевой индекс a[i]
# i = 0 # Начальная переменная для цикла

# while i < len(a):
#  if (x-a[i])**2 <= minraz:      
#   minraz = (x-a[i])**2
# b = i
# i += 1
# print('Последовательность: ', a)
# print('Самое близкое значение элемента массива: ', a[b])
# print('Индекс элемента массива: ', b)


# вариант 2

# N = int(input('Кол. чисел: '))
# a=[int(input('Ввести число: ')) for i in range(N)]
# x=int(input('Заданное число: '))
# b=[abs(a[i]-x) for i in range(len(a))]
# print(a[b.index(min(b))])

#   # Вариант 3
# n = int(input())
# list_1 = list()
# for i in range(n):
#     x = int(input())
#     list_1.append(x)

# k = int(input())
# m = abs(k - list_1[0]) 

# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)


# Задача 16:
# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь вводит натуральное число N – количество элементов в массиве и число, которое необходимо проверить - X.
# Заполните массив случайными натуральными числами от 1 до N/2.
# Выведите, сколько раз X встречается в массиве.

# Ввод: 5
# Ввод: 1

# 1 2 1 2 2
# Вывод: 2


# import random
# N = int(input('Введите размер массива N: '))
# X = int(input('Введите число X: '))
# N_array = []
# for i in range(N):
#     N_array.append(random.randint(0, N//2))
# print(f'Число вхождений посчитали с помощью встроенной функции count {N_array.count(X)}')
# print('Некорректный ввод. Попробуйте еще раз!')






# Запросить у пользователя количество вводимых чисел (n) и цифру для подсчета (d).
# Присвоить счетчику цифр значение 0.
# Выполнить n раз цикл, в теле которого
# запрашивать очередное число,
# пока это число не сократиться до нуля
# извлекать последнюю его цифру и сравнивать с цифрой, которую надо посчитать,
# увеличивать значение счетчика цифр на 1, если сравниваемые цифры совпадают,
# избавляться от последней цифры числа.
# В конце программы вывести количество посчитанных цифр на экран.




# n = int(input("Сколько будет чисел? "))
# d = int(input("Какую цифру считать? "))
# count = 0
# for i in range(1,n+1):
#      m = int(input("Число " + str(i) + ": "))
#      while m > 0:
#         if m%10 == d:
#             count += 1
#         m = m // 10
 
# print("Было введено %d цифр %d" % (count, d))


#----------------------------------------------------------------------------------------------

# is_dark = input('На улице темно?д/н)')
# if is_dark == 'д':
#         print('Спокойной ночи! Хр-р-р-р-р..')
# else:
#         print('ептить')



# dict_with_letter = {1: ("А","Е","В","И","Н","О","Р","С","Т", 
#  'A','E','I','O','U','L','N','S','T','R'), 
#  2: ("Д","К","Л","М","П","У", 
#  'D', 'G'), 
#  3: ("Б","Г","Ё","Ь","Я", 
#  'B','C','M', 'P'), 
#  4: ("Й","Ы", 
#  'F', 'H', 'V', 'W', 'Y'), 
#  5: ("Ж","З","Х","Ц","Ч", 
#  'K'), 
#  6: ("Ш", "Э","Ю", 
#  'J','X'), 
#  7: ("Ф","Щ","Ъ", 
#  'Q','Z') 
#  } 
 
# def dicting(dict_with, words): 
#  sum_points = 0 
#  for key, value in dict_with.items(): 
#   for letter in words.upper(): 
#    if letter in value: 
#     sum_points += key 
#  print(sum_points) 
# word = str(input()) 
# dicting(dict_with_letter,word)





# Задача 22:
# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого набора.
# m - кол-во элементов второго набора.
# Значения генерируются случайным образом.

# Input: 11 6
# (значения сгенерированы случайным образом
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18)

# Output: 11 6
# 6 12


# def create_array(n, mn, mx):
#     import random
#     array = [random.randint(mn, mx) for _ in range(n)]
#     return array


# n = int(input('Кол-во элементов первого набора? -> '))
# m = int(input('Кол-во элементов второго набора? -> '))
# listing_1 = create_array(n, 2, 13)
# listing_2 = create_array(m, 2, 13)
# print(listing_1)
# print(listing_2)

# set_1 = set(listing_1)
# set_2 = set(listing_2)

# result = set_1 & set_2
# print('Пересечение множеств - ', sorted(result), '\n')



# Вариант 2 Задача 22

# import random

# n = int(input('Введите кол-во элементов первого набора: '))
# m = int(input('Введите кол-во элементов второго набора: '))

# first_list = [(random.randint(-20, 20)) for i in range(n)]
# print(first_list)
# second_list = [(random.randint(-20, 20)) for i in range(m)]
# print(second_list)


# result = []
# for item in set(first_list):
#     if item in set(second_list):
#         result.append(item)

# for i in range(len(result)-1):
#     for j in range(len(result)-i-1):
#         if result[j] > result[j+1]:
#             result[j], result[j+1] = result[j+1], result[j]

# if len(result) < 1:
#     print('Общих элементов в данных наборах нет')
# else:
#     print(result)






# Задача 24:
# В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке,
# причем кусты высажены только по окружности. Таким образом, у каждого куста
# есть ровно два соседних. Всего на грядке растет N кустов. 
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора
# на них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. 
# Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, 
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод, которое может 
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.

# Input: 4
# (значения сгенерированы случайным образом
# 4 2 3 1 )

# Output: 9



# import random
# kust = int(input("введите количество кустов: "))
# berryes = list(random.randint(0, 10) for i in range(kust))
# result = []
# i = 0
# sum = 0

# print(berryes)

# while (i < kust):
#     if (i == kust - 1):
#         sum = berryes[i] + berryes[i - 1] + berryes[0]
#     else:
#         sum = berryes[i] + berryes[i - 1] + berryes[i + 1]
#         result.append(sum)
#         result.sort()
#     i += 1

# print(f"максимальное число ягод за одну итерацию {result[-1]}")






# Задача 26:
# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.



# x = int(input(' Введите число A: '))
# y = int(input(' Введите число B: '))

# def pov(a, n):
#     if (n == 1):
#         return a
#     else:
#         return a * pow(x, n - 1)
# print(pov(x, y))


# # Задача 102 
# # Задайте натуральное число N. Напишите программу, которая составит список простых
# множителей числа N.
# print("Задайте натуральное число N. Напишите программу, которая составит
# список простых множителей числа N.")

# num = int(input("Введите число: "))
# i = 2 # первое простое число
# lst = []
# old = num
# while i <= num:
#     if num % i == 0:
#         lst.append(i)
#         num //= i
#         i = 2
#     else:
#         i += 1
# print(f"Простые множители числа {old} приведены в списке: {lst}")


# Задача 101 
# Вычислить число π c заданной точностью d

# import math
# import os
# os.system('cls')
# print('число Pi c заданной точностью d, round()')
# d = int(input(' степень округления количество знаков после запятой  '))
# pi_round = int(math.pi * 10**d) /10**d
# print(pi_round)


# Задача 105
# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

# text = 'абв кот парк абв столб'
# text_find = 'абв'
# index = 0

# list1 = text.split(' ')
# print(list1)

# list2 = [item for item in list1 if text_find not in item]
# print(list2)





# Задача 106
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента? (Добавьте игру против бота)


# from random import randint

# def input_dat(name):
#     x = int(input(f"{name}, введите количество конфет, которое возьмете от 1 до 28: "))
#     while x < 1 or x > 28:
#         x = int(input(f"{name}, введите корректное количество конфет: "))
#     return x


# def p_print(name, k, counter, value):
#     print(f"Ходил {name}, он взял {k}, теперь у него {counter}. На столе еще осталось {value} конфет.")

# player1 = input("Введите имя первого игрока: ")
# player2 = input("Введите имя второго игрока: ")
# value = int(input("Укажите количество конфет на столе: "))
# flag = randint(0, 2)
# if flag:
#     print(f"Первым ходит {player1}")
# else:
#     print(f"Первым ходит {player2}")

# counter1 = 0 
# counter2 = 0

# while value > 28:
#     if flag:
#         k = input_dat(player1)
#         counter1 += k
#         value -= k
#         flag = False
#         p_print(player1, k, counter1, value)
#     else:
#         k = input_dat(player2)
#         counter2 += k
#         value -= k
#         flag = True
#         p_print(player2, k, counter2, value)

# if flag:
#     print(f"{player1} урвал победу! Поздравляем!")
# else:
#     print(f"{player2} урвал победу! Поздравляем!")



# Задача 107
# Создайте программу для игры в ""Крестики-нолики"" (Добавьте игру против бота)


# import tkinter.messagebox
# from tkinter import *
# import os
# os.system('cls')


# # выход из приложения

# def exit_(event):
#     root.destroy()


# # начать заново
# def begin(event):
#     global butn
#     global field
#     global numButton
#     for b in butn:
#         b.config(bg="green", text='')
#     field = [0, 0, 0, 0, 0, 0, 0, 0, 0]
#     numButton = []


# # логика приложения
# def logik():
#     global field
#     global numButton
#     if len(numButton) == 9:
#         tkinter.messagebox.showinfo("Конец игры", "  Ничья!!!  ")
#     else:
#         end = False
#         if field[0] == field[1] == field[2] > 0:
#             winner = field[0]
#             end = True
#         elif field[3] == field[4] == field[5] > 0:
#             winner = field[3]
#             end = True
#         elif field[6] == field[7] == field[8] > 0:
#             winner = field[6]
#             end = True
#         elif field[0] == field[3] == field[6] > 0:
#             winner = field[0]
#             end = True
#         elif field[1] == field[4] == field[7] > 0:
#             winner = field[1]
#             end = True
#         elif field[2] == field[5] == field[8] > 0:
#             winner = field[2]
#             end = True
#         elif field[0] == field[4] == field[8] > 0:
#             winner = field[0]
#             end = True
#         elif field[2] == field[4] == field[6] > 0:
#             winner = field[2]
#             end = True
#         if end:
#             if winner == 1:
#                 user = "O"
#             elif winner == 2:
#                 user = "X"
#             tkinter.messagebox.showinfo("Конец игры", "Выиграл " + user)
#             begin(None)

# # нажатие на кнопки


# def click(button, num):
#     global numButton
#     if num not in numButton:
#         global XO
#         if XO == 1:
#             button.config(text='O')
#             button.config(bg='blue')
#             field[num] = XO
#             XO = 2
#         else:
#             button.config(text='X')
#             button.config(bg='red')
#             field[num] = XO
#             XO = 1
#         numButton.append(num)
#         logik()


# field = [0, 0, 0, 0, 0, 0, 0, 0, 0]  # список значений 1 или 2
# XO = 1  # крестик - 1, нолик - 2
# numButton = []  # список нажатых кнопок


# root = Tk()
# root.title("Крестики-нолики")
# root.geometry("233x238")
# root.resizable(False, False)

# ris0 = Button(root, width=10, height=5, bg="green",
#                command=lambda: click(ris0, 0)) 
# ris0.place(x=0, y=0)
# ris1 = Button(root, width=10, height=5, bg="green",
#                command=lambda: click(ris1, 1))
# ris1.place(x=81, y=0)
# ris2 = Button(root, width=10, height=5, bg="green",
#                command=lambda: click(ris2, 2))
# ris2.place(x=162, y=0)

# ris3 = Button(root, width=10, height=5, bg="green",
#                command=lambda: click(ris3, 3))
# ris3.place(x=0, y=81)
# ris4 = Button(root, width=10, height=5, bg="green",
#                command=lambda: click(ris4, 4))
# ris4.place(x=81, y=81)
# ris5 = Button(root, width=10, height=5, bg="green",
#                command=lambda: click(ris5, 5))
# ris5.place(x=162, y=81)

# ris6 = Button(root, width=10, height=5, bg="green",
#                command=lambda: click(ris6, 6))
# ris6.place(x=0, y=162)
# ris7 = Button(root, width=10, height=5, bg="green",
#                command=lambda: click(ris7, 7))
# ris7.place(x=81, y=162)
# ris8 = Button(root, width=10, height=5, bg="green",
#                command=lambda: click(ris8, 8))
# ris8.place(x=162, y=162)

# butn = [ris0, ris1, ris2, ris3, ris4, ris5, ris6, ris7, ris8]


# root.mainloop()



# #Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.
#

# def coder(line: str) -> str:
#     encoding_line = ''
#     count = 1
#     temp = line[0]
#     for i in range(1, len(line)):
#         if line[i] == temp:
#             count += 1
#         else:
#             encoding_line += str(count) + temp
#             temp = line[i]
#             count = 1
#         # кодировка последнего элемента
#         if i == (len(line) - 1):
#             encoding_line += str(count) + temp
#     return encoding_line


# def decoder(line: str) -> str:
#     decoder_line = ''
#     for i in range(0, len(line), 2):
#         decoder_line += line[i + 1] * int(line[i])
#     return (decoder_line)

# line = 'WWJJJHDDDDDPPGRRR'

# print("Исходная строка: ", line)
# code_line = coder(line)
# print("Закодированная строка: ", code_line)
# print("Декодированная строка: ", decoder(code_line))


