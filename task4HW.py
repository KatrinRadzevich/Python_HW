# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое
# количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10
# 7 -> "нельзя определить"
allBirdsQuantity = int(
    input('Введите количество всех сделанных журавликов детьми: '))
if allBirdsQuantity % 2 == 0 and allBirdsQuantity % 3 == 0:
    quantityOfPeterAndSerge = int(allBirdsQuantity/3)
    quantityOfKate = int(quantityOfPeterAndSerge * 2)
    quantityOfPeter = int(quantityOfPeterAndSerge/2)
    quantityOfSerge = int(quantityOfPeter)
    print(f'{allBirdsQuantity} -> {quantityOfPeter} {quantityOfKate} {quantityOfSerge}')
else:
    print('"нельзя определить"')
