# Реализуйте алгоритм перемешивания списка (shuffle использовать нельзя,
# другие методы из библиотеки random - можно)

import random

N = int(input('Enter number: '))
a = []
for i in range(N + 1):
    a.append(i)
print('Initial list:', a)
for i in range(random.randrange(1, N)):
    t1, t2 = random.randint(1, N), random.randint(1, N)
    a[t1], a[t2] = a[t2], a[t1]
print('Jumbled list:', a)