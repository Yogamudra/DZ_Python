# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

decimal = int(input('Enter number: '))
binary = ''
while decimal > 0:
    binary = str(decimal%2) + binary
    decimal = decimal // 2
print(binary)



