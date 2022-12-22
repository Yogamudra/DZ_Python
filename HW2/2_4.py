# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

N = int(input())
list = []
for i in range(-N, N + 1):
    list.append(i)
print(list)

p = 1
with open('2_4.txt') as f:
    for i in f.readlines():
        p *= list[int(i)]

print(p)