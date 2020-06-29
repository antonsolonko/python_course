# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

# TODO здесь ваш код
def figure(amount_of_angles, color, point=sd.get_point(200,150), angle=0, length=200):
    last_point_skleika = point
    step = int(360 / amount_of_angles)
    for x in range(0, 360 - step, step):
        v1 = sd.get_vector(start_point=point, angle=angle + x, length=length, width=1)
        v1.draw(color=color)
        sd.circle(center_position=v1.end_point, color=color, radius=30)
        point = v1.end_point # переход на следующюю точку
    else:
        sd.line(start_point=point, color=color, end_point=last_point_skleika, width=1)
        sd.circle(center_position=last_point_skleika, color=color, radius=30)

figures = ['Triangle','Square','Pentagon','Hexagon']
my_colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                   sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
colors_number = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan', 'Blue', 'Purple']

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

print('Выберите цвет из списка по номеру:\n')
i=0
for _ in colors_number:
    print(_,i)
    i +=1
while True:
    user_color = int(input())
    if user_color in [0,1,2,3,4,5,6]:
        color = my_colors[ user_color ]
        print('Вы выбрали цвет номер:', user_color, '-', my_colors[user_color])
        break
    else:
        print('Введите номер еще раз\n')

figure(amount_of_angles, color)


sd.pause()
