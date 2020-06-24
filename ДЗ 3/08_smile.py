# -*- coding: utf-8 -*-

# (определение функций)

import random
import simple_draw as sd
sd.resolution = (1200, 600)

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

#здесь ваш код

def smile(x, y, color):
    left_bottom = sd.get_point(x - 70, y -45)
    right_top = sd.get_point(x + 70, y + 45)
    sd.ellipse(left_bottom = left_bottom, right_top = right_top, color = color, width = 3) # Голова
    left_eye = sd.get_point(x - 15, y)
    right_eye = sd.get_point(x + 15, y)
    sd.circle(center_position = left_eye, radius = 15, color=color, width = 2)   # левый глаз
    sd.circle(center_position = right_eye,radius=15, color = color,width = 2)   # правый глаз
    sd.lines(point_list = point_list, color = color, width = 2, closed = False)     # улыбка



for _ in range(10000):
    x = sd.randint(1, 1200)
    y = sd.randint(1, 600)
    color = sd.random_color()
    point_list = [sd.get_point(x - 20, y - 25),      # список координат для улыбки
                  sd.get_point(x - 5, y - 35),
                  sd.get_point(x + 5, y - 35),
                  sd.get_point(x + 20, y - 25)]
    smile(x, y, color)

sd.pause()
