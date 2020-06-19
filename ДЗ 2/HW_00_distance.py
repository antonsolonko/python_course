#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480), #Переменные определены как tuple
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()



moscow = sites['Moscow'] #взяли координаты Москвы
london = sites['London']
paris = sites['Paris']
moscow_london = ((moscow[0] - london[0])**2 + (moscow[1] - london[1])**2) ** .5 #по формуле нужно взять корень, возводим в степень .5
moscow_paris = ((moscow[0] - paris[0])**2 + (moscow[1] - paris[1])**2) ** .5

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_london
distances['Moscow']['Paris'] = moscow_paris

london_paris = ((paris[0] - london[0])**2 + (paris[1] - london[1])**2) ** .5
print(type(paris))
distances['London'] = {}
distances['London']['Moscow'] = moscow_london
distances['London']['Paris'] = london_paris

distances['Paris'] = {}
distances['Paris']['Moscow'] = moscow_london
distances['Paris']['London'] = london_paris

pprint(distances['Moscow']['Paris'])

# пробую комиты
# пробую комиты еще раз


