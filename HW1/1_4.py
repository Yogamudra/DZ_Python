# Напишите программу, которая по заданному номеру четверти
# показывает диапазон возможных координат точек в этой четверти (x и y)

a = int(input('Specify a quarter (a number from 1 to 4): '))
if a == 1:
    print('x>0, y>0')
elif a == 2:
    print('x<0, y>0')
elif a == 3:
    print('x<0, y<0')
else:
    print('x>0, y<0')

