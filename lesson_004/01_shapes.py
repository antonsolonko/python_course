# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника

# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# TODO здесь ваш код
def triangle(point, angle, length):
    last_point_skleika = point
    for x in range(0,360 - 120,120):
        v1 = sd.get_vector(start_point=point,angle=angle + x,length=length,width=1)
        v1.draw()
        point = v1.end_point
    else:
        sd.line(start_point=point,end_point=last_point_skleika,width=1)


def square(point, angle, length):
    last_point_skleika = point
    for x in range(0,360 - 90,90):
        v1 = sd.get_vector(start_point=point,angle=angle + x,length=length,width=1)
        v1.draw()
        point = v1.end_point
    else:
        sd.line(start_point=point,end_point=last_point_skleika,width=1)

def pentagon(point, angle, length):
    last_point_skleika = point
    for x in range(0,360 - 72,72):
        v1 = sd.get_vector(start_point=point,angle=angle + x,length=length,width=1)
        v1.draw()
        point = v1.end_point
    else:
        sd.line(start_point=point,end_point=last_point_skleika,width=1)


def hexagon(point, angle, length):
    last_point_skleika = point
    for x in range(0,360 - 60,60):
        v1 = sd.get_vector(start_point=point,angle=angle + x,length=length,width=1)
        v1.draw()
        point = v1.end_point
    else:
        sd.line(start_point=point,end_point=last_point_skleika,width=1)


square(point = sd.get_point(400, 400), angle = 15, length = 150)
triangle(point = sd.get_point(50, 50), angle = 15, length = 150)
pentagon(point = sd.get_point(100, 350), angle = 15, length = 120)
hexagon(point = sd.get_point(400, 50), angle = 15, length =100)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

# =============== Нужно отдельно выделить функцию соединения точек, то есть тип соединения.
# Круг в угловой точке-можно по номеру угла в фигуре - проверка или рисуем круг по координатам или возвращаем None

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв
#   в начальной/конечной точках рисуемой фигуры (если он есть)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
