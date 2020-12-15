import tkinter
import math
# Параметры
angleBetween = 22
lenFactor = 0.8
startLength = 100
minLength = 6

# Подготовим окно вывода
root = tkinter.Tk()
width, height = 1100, 500
c = tkinter.Canvas(root, width=width, height=height)
c.pack()

def branch(point, angle, length):
    # Условие выхода из рекурсии
    if (length < minLength): return

    # Вычислим и нормализуем углы на которые направлены новые ветки
    # Нормализовать угол,значит преобразовать его к промежутку от 0 до 360 градусов
    lb_angle = normalize(angle + angleBetween)
    rb_angle = normalize(angle - angleBetween)

    x, y = point[0], point[1]
    # Получим точки в которые нужно провести линии
    lb_point = getBranchEnding(x, y, lb_angle, length)
    rb_point = getBranchEnding(x, y, rb_angle, length)

    # Узнаем насколько близко длина новых веток к минимальноей
    # и в соответствии с этим зададим толщину линий
    branch_width = 10 * ((length - minLength) / (startLength - minLength))
    c.create_line(x, y, lb_point[0], lb_point[1], width=branch_width, fill='green')
    c.create_line(x, y, rb_point[0], rb_point[1], width=branch_width, fill='green')

    # Рекурсивно генерируем следующие ветки
    branch(lb_point, lb_angle, length * lenFactor)
    branch(rb_point, rb_angle, length * lenFactor)

# Функция, возвращающая кортеж с координатами точки конца очередной ветки
def getBranchEnding(x, y, angle, length):
    return (
        x - (math.sin(math.radians(angle)) * length),
        y - (math.cos(math.radians(angle)) * length))

def normalize(angle):
    while (angle < 0):
        angle += 360
    while (angle >= 360):
        angle -= 360
    return angle

if (__name__ == '__main__'):
    # Отрисуем ствол дерева
    root_x = width / 2
    root_y = height * 0.98
    x = root_x
    y = root_y - startLength
    c.create_line(root_x, root_y, x, y, fill='green', width = 10)

    # Запустим рекурсию, передав начальные значения
    # Для выполнения условия самододобия первые
    # две ветки должны быть короче ствола
    branch((x, y), 0, startLength * lenFactor)
    root.mainloop()