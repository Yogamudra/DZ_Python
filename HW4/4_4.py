# Задана натуральная степень k.
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена
# и записать в файл многочлен степени k.

import random
k = int(input("Specify the degree K: "))
polynomial = ''
for i in range(k):
    coefficients = random.randint(0, 100)
    if coefficients == 1:
        if k - i > 1:
            polynomial += 'x^' + str(k - i)
        else:
            polynomial += 'x'
    if coefficients > 1:
        if k - i > 1:
            polynomial += str(coefficients) + '*x^' + str(k - i)
        else:
            polynomial += str(coefficients) + '*x'
    if i != k - 1:
        polynomial += '+'

print(polynomial)