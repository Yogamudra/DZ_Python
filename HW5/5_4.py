# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных

def coding(txt):
    count = 1
    res = ''
    for i in range(len(txt)-1):
        if txt[i] == txt[i+1]:
            count += 1
        else:
            res = res + str(count) + txt[i]
            count = 1
    if count > 1 or (txt[len(txt)-2] != txt[-1]):
        res = res + str(count) + txt[-1]
    return res

def decoding(txt):
    number = ''
    res = ''
    for i in range(len(txt)):
        if not txt[i].isalpha():
            number += txt[i]
        else:
            res = res + txt[i] * int(number)
            number = ''
    return res


with open('coding.txt', 'r') as data:
    my_text = data.read()
print(f"Текст после кодировки: {coding(my_text)}")
with open('encoding.txt', 'r') as data:
    my_text2 = data.read()
print(f"Текст после дешифровки: {decoding(my_text2)}")