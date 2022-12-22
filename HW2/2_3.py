# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму

n = int(input('Enter sequence value: '))
s = 0
for i in range(n):
    s = s + ((1 + 1 / n)**n)
print('Sum of sequence numbers: ', round(s, 2))