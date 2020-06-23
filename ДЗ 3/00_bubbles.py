# -*- coding: utf-8 -*-
import random

import simple_draw as sd  # вызов ф-ии из библиотеки sd.circle() sd.get_point()

sd.resolution = (1200, 600)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
# point = sd.get_point(300, 300)
# radius = 50
# for _ in range(3):
#     radius +=5
#     sd.circle(center_position=point, radius=radius, width=2)    #внутренней переменной radius присваиваю внешнюю переменную radius

# Написать функцию рисования пузырька, принммающую 2 (или более) параметра: точка рисовании и шаг
# def bubble(point, step):   # ф-я пузырька
#     radius = 50             # изначальный радиус первового пузырька
#     for _ in range(3):      # цикл для рисования трех вложенных пузырьков
#         radius += step      # инкрементируем шаг рисования радиуса
#         sd.circle(center_position=point, radius=radius, width=2) #ф-я рисиования круга: координаты=центр круга, радиус, толщина линии
# #функция пузырька определена
# point = sd.get_point(300,300)  # координаты стартовой точки
# bubble(point=point,step=10)    # вызываб ф-ю и передаю параметры для стартовой точки и шаг инкрементации радиуса

# Нарисовать 10 пузырьков в ряд
# for x in range(100,1101,100):
#     radius = 45
#     point = sd.get_point(x, 100) # ф-я стартовой точки - Y-ветрикаль статичные координаты, X-вертикаль смещается на 100 пунктов
#     sd.circle(center_position=point, radius=radius, width=2) #
#--------------------
# def bubble(point, step):   # ф-я пузырька
#     radius = 50             # изначальный радиус первового пузырька
#     for _ in range(3):      # цикл для рисования трех вложенных пузырьков
#         radius += step      # инкрементируем шаг рисования радиуса
#         sd.circle(center_position=point, radius=radius, width=2) #ф-я рисиования круга: координаты=центр круга, радиус, толщина линии
# for x in range(100,1001,100):
#     point = sd.get_point(x, 100)
#     bubble(point=point, step = 5)

# Нарисовать три ряда по 10 пузырьков
# def bubble(point, step):   # ф-я пузырька
#     radius = 50             # изначальный радиус первового пузырька
#     for _ in range(3):      # цикл для рисования трех вложенных пузырьков
#         radius += step      # инкрементируем шаг рисования радиуса
#         sd.circle(center_position=point, radius=radius, width=2) #ф-я рисиования круга: координаты=центр круга, радиус, толщина линии
# for y in range(100,301,100):
#     for x in range(100,1001,100):
#         point= sd.get_point(x,y)
#         bubble(point=point, step=5)

# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
def bubble(point, step):   # ф-я пузырька
    radius = 50             # изначальный радиус первового пузырька
    for _ in range(3):      # цикл для рисования трех вложенных пузырьков
        radius += step      # инкрементируем шаг рисования радиуса
        sd.circle(center_position=point, radius=radius, color=color, width=2) #ф-я рисиования круга: координаты=центр круга, радиус, толщина линии
for _ in range(100):
    point = sd.random_point()
    step = random.randint(2,10)  # ввожу random затем alt+enter выбираю импорт функции
    color = sd.random_color()
    bubble(point=point, step=step)

sd.pause()
