# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

realNumber = input('Enter number: ')
s = 0
for i in realNumber:
    if i.isdigit():
        s += int(i)

print(s)