# 25'. Напишите программу, которая принимает на вход строку, и
# отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса
# формата _n. Порядок символов исходной строки не меняется.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
a = 'a a a b c a a d c d d'.split()
dict_count = {}
list_count = []
for i in a:
    if i in list_count:
        dict_count[i] = dict_count.get(i, 0) + 1
        list_count.append(f'{i}_{dict_count[i]}')
    if i not in list_count:
        list_count.append(i)


print(list_count)
