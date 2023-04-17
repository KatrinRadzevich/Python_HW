# *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:A, E, I, O, U, L, N, S, T, R – 1 очко;
# D, G – 2 очка; B, C, M, P – 3 очка; F, H, V, W, Y – 4 очка; K – 5 очков; J, X – 8 очков; Q,
# Z – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит только английские,
# буквы.
# *Пример:*
# laptop
#     10

word = input('Введите слово на английском,чтобы унать его ценность: ')
count = 0
for ind in word:
    if ind == 'a' or ind == 'e' or ind == 'i' or ind == 'o' or ind == 'u':
        count += 1
    elif ind == 'l' or ind == 'n' or ind == 's' or ind == 't' or ind == 'r':
        count += 1
    elif ind == 'd' or ind == 'g':
        count += 2
    elif ind == 'b' or ind == 'c' or ind == 'm' or ind == 'p':
        count += 3
    elif ind == 'f' or ind == 'h' or ind == 'v' or ind == 'w' or ind == 'y':
        count += 4
    elif ind == 'k':
        count += 5
    elif ind == 'j' or ind == 'x':
        count += 8
    elif ind == 'z':
        count += 10
print(count)
