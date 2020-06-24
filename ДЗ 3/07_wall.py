# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd
from simple_draw import Point

sd.resolution = (1200, 600)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

# TODO здесь ваш код
x = 0
y = 0
null = 0
for y in range(0,600,50):
    if null == 0:
       null = -50
    else:
        null = 0
    for x in range(null,1201,100):
        x1 = x + 100
        y1 = y + 50
        left_bottom = sd.get_point(x,y)
        right_top = sd.get_point(x1,y1)
        sd.rectangle(left_bottom=left_bottom,right_top=right_top,color=sd.COLOR_ORANGE,width=1)

sd.pause()
