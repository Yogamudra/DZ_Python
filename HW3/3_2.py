# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

lst1 = [int(i) for i in input('Enter list of numbers: ').split()]
print(lst1)
lst2 = []
count = len(lst1)
for i in range(len(lst1)):
    while i < len(lst1)/2 and count > len(lst1)/2:
        count = count - 1
        pair = lst1[i] * lst1[count]
        lst2.append(pair)
        i += 1
print(lst2)