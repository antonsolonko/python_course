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

# здесь ваш код
# def triangle(point, angle, length):
#     v1 = sd.get_vector(start_point = point, angle = angle, length = length, width = 1)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point = v1.end_point, angle = angle + 120, length = length, width = 1)
#     v2.draw()
#
#     sd.line(start_point = v2.end_point, end_point=point, width = 1)
#
#
# def square(point, angle, length):
#     v1 = sd.get_vector(start_point = point, angle = angle, length = length, width = 1)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point = v1.end_point , angle = angle + 90, length = length, width = 1)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point = v2.end_point, angle = angle + 180, length = length, width = 1)
#     v3.draw()
#
#     sd.line(start_point = v3.end_point, end_point=point, width = 1)
#
# def pentagon(point, angle, length):
#     v1 = sd.get_vector(start_point = point, angle = angle, length = length, width =1)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point = v1.end_point, angle = angle + 72, length = length, width = 1)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point = v2.end_point, angle= angle + 144, length = length, width = 1)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point = v3.end_point, angle= angle + 216, length = length, width = 1)
#     v4.draw()
#
#     sd.line(start_point = v4.end_point, end_point=point, width = 1)
#
#
# def hexagon(point, angle, length):
#     v1 = sd.get_vector(start_point = point, angle = angle, length = length, width = 1)
#     v1.draw()
#
#     v2 = sd.get_vector(start_point = v1.end_point, angle = angle + 60, length = length, width = 1)
#     v2.draw()
#
#     v3 = sd.get_vector(start_point = v2.end_point, angle = angle + 120, length = length, width = 1)
#     v3.draw()
#
#     v4 = sd.get_vector(start_point = v3.end_point, angle= angle + 180, length = length, width = 1)
#     v4.draw()
#
#     v5 = sd.get_vector(start_point = v4.end_point, angle = angle + 240, length = length, width = 1)
#     v5.draw()
#
#     sd.line(start_point = v5.end_point, end_point=point, width = 1)
#
#
#
# square(point = sd.get_point(400, 400), angle = 15, length = 150)
# triangle(point = sd.get_point(50, 50), angle = 15, length = 150)
# pentagon(point = sd.get_point(100, 350), angle = 15, length = 120)
# hexagon(point = sd.get_point(400, 50), angle = 15, length =100)


# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44?

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

# square(point = sd.get_point(400, 400), angle = 15, length = 150)
# triangle(point = sd.get_point(50, 50), angle = 15, length = 150)
# pentagon(point = sd.get_point(100, 350), angle = 15, length = 120)
# hexagon(point = sd.get_point(400, 50), angle = 15, length =100)

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

def figure(amount_of_angles, point=sd.get_point(200,150), angle=0, length=200):
    last_point_skleika = point
    step = int(360 / amount_of_angles)
    for x in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + x, length=length, width=1)
        v1.draw()
        sd.circle(center_position=v1.end_point, radius=30)
        point = v1.end_point # переход на следующюю точку
    else:
        sd.line(start_point=point, end_point=last_point_skleika, width=1)
        sd.circle(center_position=last_point_skleika,radius=30)

figures = ['Triangle','Square','Pentagon','Hexagon']
print('Выберите фигуру из списка по номеру:\n',
'1. Triangle\n',
'2. Square\n',
'3. Pentagon\n',
'4. Hexagon\n'
)

while True:
    user_input = input()
    amount_of_angles = int(user_input)+2
    if amount_of_angles in [3,4,5,6]:
            print('Вы выбрали фигуру номер:', user_input, '-', figures[amount_of_angles-3])
            break
    else:
             print('Введите номер еще раз\n')
figure(amount_of_angles)


# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
