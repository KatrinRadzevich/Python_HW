list_1 = [12, 7, -1, 21, 0]
print(list_1.pop())  # 0
print(list_1)  # [12, 7, -1, 21]
print(list_1.pop())  # 21
print(list_1)  # [12, 7, -1]
print(list_1.pop())  # -1
print(list_1)  # [12, 7]

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[0])  # 1
print(list_1[1])  # 2
print(list_1[len(list_1)-1])  # 10
print(list_1[-5])  # 6
print(list_1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list_1[:2])  # [1, 2]
print(list_1[len(list_1)-2:])  # [9, 10]
