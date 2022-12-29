# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def find_power(a):
    t = a.split('x')
    if t[0]:
        return int(t[0])
    return 1

with open('File01.txt', 'r') as f:
    m1 = f.readlines()[0]

with open('File02.txt', 'r') as f:
    m2 = f.readlines()[0]

k1 = []
for i in m1.split('+'):
    k1.append(find_power(i))

k2 = []
for i in m2.split('+'):
    k2.append(find_power(i))

k1 = [0] * (max(len(k2), len(k1)) - len(k1)) + k1
k2 = [0] * (max(len(k2), len(k1)) - len(k2)) + k2

res = []
for i in range(len(k1)):
    res.append(k1[i] + k2[i])

out = ''
for i in range(len(res)):
    koef = res[i]
    if koef == 1:
        if len(res) - i > 1:
            out += 'x^' + str(len(res) - i)
        else:
            out += 'x'
    if koef > 1:
        if len(res) - i > 1:
            out += str(koef) + '*x^' + str(len(res) - i)
        else:
            out += str(koef) + '*x'
    if i != len(res) - 1:
        out += '+'

with open('res.txt', 'w') as f:
    f.write(out)