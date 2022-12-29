# Задайте последовательность чисел.
# Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

lst01 = list(map(int, input("Enter a sequence of numbers separated by a space:\n").split()))
print(f"Original sequence: {lst01}")
lst02 = []
[lst02.append(i) for i in lst01 if i not in lst02]
print(f"list of non-repeating elements of the original sequence: {lst02}")