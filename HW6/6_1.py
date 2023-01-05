# Наибольший общий делитель
# В модуле math есть функция math.gcd(a, b), возвращающая наибольший общий делитель (НОД) двух чисел.

# Вычислите и напечатайте наибольший общий делитель для списка натуральных чисел.
# Ввод чисел продолжается до ввода пустой строки.
# Входные данные Выходные данные
# 36
# 12
# 144
# 18 6

import math
import functools

numbers = []
while True:
    tmp = input('Enter number: ')
    if tmp:
        numbers.append(int(tmp))
    else:
        break

print(f"Greatest common divisor: {functools.reduce(lambda x, y: math.gcd(x, y), numbers)}")