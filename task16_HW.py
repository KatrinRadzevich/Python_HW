# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1

n = int(input('Введите размер массива: '))
a = []
for i in range(1, n + 1):
    a.append(i)
print(a)
x = int(input('Введите искомое число в массива: '))
print(f'-> {a.count(x)}')