# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

f = int(input('Enter the size of the Fibonacci number: '))
if f < 0: f = f*-1
f1 = f2 = 1
list = [f1, f2]
for i in range(2, f):
    f1,f2 = f2, f1 + f2
    list.append(f2)
print(list)
f1=f2=1
for i in range(-f, 1):
    f1,f2 = f2, f1 - f2
    list.insert(0, f2)
print(list)