# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

lst = [int(i) for i in input('Enter list of numbers: ').split()]
print(lst)
summa = 0
for i in range(0, len(lst), 2):
    summa = summa + lst[i]
print(summa)