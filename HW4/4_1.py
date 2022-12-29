# Вычислить число c заданной точностью d
from math import pi

d =  int(input("Set number precision: "))
print(f'The number pi with a given accuracy {d} is equal to {round(pi, d)}')
