# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b, i = 179, 37, 0

# TODO здесь ваш код
while a > b:
    i += 1
    a -= b
print('Целочисленное деление a на b дает', i)
