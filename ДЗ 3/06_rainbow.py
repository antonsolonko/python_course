# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
# здесь ваш код
# a,b=50,450
# for color in rainbow_colors:
#     point1 = sd.get_point(50, a)
#     point2 = sd.get_point(1050, b)
#     current_color = color
#     sd.line(start_point=point1, end_point=point2, color=current_color, width=9)
#     a+=10
#     b+=10
# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# здесь ваш код
center = sd.get_point(800, -400)
radius = 800

for color in rainbow_colors:
    current_color = color
    sd.circle(center_position=center, radius=radius, color=current_color, width=25)
    radius += 25

sd.pause()
