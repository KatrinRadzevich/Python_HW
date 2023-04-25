# Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз?
# Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза.
# Все числа натуральные и не превышают 30000.
import random
watermelon = int(input('Введите количество абузов: '))
watermelon_weight = random.randint(1, 30000)
print(f' Вес 1 арбуза {watermelon_weight}')
start = 1
end = watermelon
step = 1
min_weight = watermelon_weight
max_weight = watermelon_weight
for i in range(start, watermelon, step):
    watermelon_weight = random.randint(1, 30000)
    print(f' Вес {i + 1} арбуза {watermelon_weight}')
    if min_weight > watermelon_weight:
        min_weight = watermelon_weight
    if max_weight < watermelon_weight:
        max_weight = watermelon_weight
print(f"Вес лёгкого арбуза = {min_weight}")
print(f"Вес тяжёлого арбуза = {max_weight}")
# watermelon_weight = int(input(f'Введите вес {i + 1} абуза: '))
