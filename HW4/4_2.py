# Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N

N = int(input("Enter number: "))
i = 2 # первое простое число
lst = []
buffer = N
while i <= buffer:
    if buffer % i == 0:
        lst.append(i)
        buffer //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {N} составляют: {lst}")
