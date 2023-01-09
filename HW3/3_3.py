# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random

lst1 = []
lst2 = []
for i in range(random.randint(1, 10)):
    t = float('.' + str(random.randint(1, 100)))
    lst1.append(float(str(random.randint(1, 100)) + str(t)))
    lst2.append(t)

print(lst1)
print(round(max(lst2) - min(lst2), 2))