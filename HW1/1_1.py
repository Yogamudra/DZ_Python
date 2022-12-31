# Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

day = int(input('Enter a number from 1 to 7: '))
if day == 6 or day == 7:
    print('weekend')
else:
    print('weekday')