# -*- coding: utf-8 -*-


# Произвольное число параметров
print(1, 2, 3, 4, 5, 56, 6,)

# *args - Обратная операция от распаковки - "запаковка", сколько бы мы не передали позиционных параметров они все
# запакакуются в tuple *agrs на который можно будет ссылаться изнутри функции через имя agrs.
# Используется когда нам нужно чтото такое перебрать,
# Так же можно этот список передать просто параметром функции, но гибкость языка позволяет передавать и произвольное
# число параметров.

# Произвольное число позиционных параметров
def print_them_all_v1(*args):
    print('print_them_all_v1')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)


print_them_all_v1(2, 'привет', 5.6)

# распаковка
my_favorite_pets = ['lion', 'elephant', 'monkey', 'cat', 'horse']
print_them_all_v1(my_favorite_pets) # функция примет список как один элемент
print_them_all_v1(*my_favorite_pets) # функция распакует список на элементы, в данном случа 5 штук



# Key word argumets
#
# Произвольное число именованных параметров
def print_them_all_v2(**kwargs):
    print('print_them_all_v2')
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v2(name='Вася', address='Moscow')

# распаковка
my_friend = {'name': 'Вася', 'address': 'Moscow', 'age': 25}
print_them_all_v2(**my_friend)

# Если на функци наверсти курсор при нажатом ctrl+mouse click то можно перейти на определение функции

# неправильные вызовы
print_them_all_v1(name='Вася', address='Moscow') # ERROR передаем в позиционную функцию именованные параметры
print_them_all_v2('Вася', 'Moscow', 25)          # ERROR наоборот в именованную функцию передаем позиционные параметры



# Комбинация
# В определении указываем, что с начаала мы можем принять любое количество позиционных параметров, а затем любое
# количество именованных.

def print_them_all_v3(*args, **kwargs):
    print('print_them_all_v3')
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v3('Вася', 'Moscow', 25)        # OK попадут в позиционные параметры
print_them_all_v3(name='Вася', address='Moscow') # OK попадут в именованные параметры

print_them_all_v3(1000, 'рублей', name='Вася', address='Moscow') # OK 1к и рубли попадут в позиционные, а вася москоу в именованные

my_friend = {'name': 'Вася', 'address': 'Moscow'}
print_them_all_v3(1000, 'рублей', **my_friend) # Распковка так же работает

# Указываем всё вместе, самый распространенный случай
# Явные параметры, позиционные, именованные
# При создании функции можно указывать как обычные параметры, так и произвольные параметры
def print_them_all_v4(a, b=5, *args, **kwargs):
    print('print_them_all_v4')
    print('a и b:', a, b)
    print('тип args:', type(args))
    print(args)
    for i, arg in enumerate(args):
        print('позиционный параметр:', i, arg)
    print('тип kwargs:', type(kwargs))
    print(kwargs)
    for key, value in kwargs.items():
        print('именованный аргумент:', key, '=', value)


print_them_all_v4(5, 6, 7, 8, cat='мяу!')
print_them_all_v4(5, b=8, cat='мяу!')
print_them_all_v4(5, cat='мяу!', address='Moscow')
print_them_all_v4(5, b=8, 7, 8, cat='мяу!') # ERROR если уже определили именованный b=8 то по синтаксису после него уже нельзя вводить позиционные
print_them_all_v4(5, 6, b=8, cat='мяу!') # ERROR 5 попадет в a, 6 попадет в b, а затем b=8 еще раз запросит в b - так нельзя тоже
print_them_all_v4(5, cat='мяу!', address='Moscow') # 5 попадет в a, b по умолчанию = 5, кот попадет в именованный


# def print_them_all_v4(a, b=5, *args, **kwargs):
# распространенный код, например передаем в A и B параметры для базы данных, а в аргах и кваргах списки того, что надо записать
# или в базу A и B надо записать то, что будет в аргах и кваргах когда будет вызываться функция кем-то
# например для интерфейсов