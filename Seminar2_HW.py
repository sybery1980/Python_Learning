

# Домашнее задание Семинар 2

# Задача 10 
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть.

# 5 -> 1 0 1 1 0
# 2

# from random import randint
# countN = int(input("Введите число монеток: "))
# tails = 0
# eagle = 0
# count = 0
# for i in range(countN):
#     x = randint(0, 1)
#     if x == 0:
#         eagle += 1
#     else:
#         tails += 1
#     print(x)
# if eagle >= tails:
#     count = countN - eagle
# else:
#     count = countN - tails
# print('Минимальное количество монет, которые нужно перевернуть:', count)



# Задача 12 
# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. 
# Помогите Кате отгадать задуманные Петей числа.

#   x + y = S
#   x * y = P
#   x = S - y (S-y)*(y)== P

# S = int(input('Введите  сумму чисел: '))
# P = int(input('Введите произведение чисел: '))
# c = 0
# for x in range (0, 1000):
#     if c: break
#     for y in range (0, 1000):
#         if x + y == S and x * y == P:
#             c = 1
#             print(x)
#             print(y)
#             break
# else:
#     print('Ошибка.Введите другие числа! ')        
            


# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.


# n =int(input('Введите число: '))
# p = 1
# while p <= n:
#     print(p)
#     p = p * 2
