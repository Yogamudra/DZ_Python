# Задайте список из нескольких чисел.
# Напишите программу, которая найдёт
# сумму элементов списка, стоящих на нечётной позиции.

import random

a = [random.randint(2, 7) for i in range(random.randint(5, 10))]
print(a)
print(sum([a[i] for i in  range(len(a)) if not i % 2]))