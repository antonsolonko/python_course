#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = []                    #ЭТО СПИСОК


# список списков приблизителного роста членов вашей семьи
my_family_height = [              #ЭТО СПИСОК СПИСКОВ
    # ['имя', рост],
    [],
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см
my_family = ['Mom','Dad','Bro','Sis','Cat','Dog','Me']
my_family_height = [
    ['Mom', 160], ['Dad', 175], ['Bro', 172], ['Sis', 168],
    ['Cat', 23], ['Dog', 54], ['Me', 187],
]
print('Рост отца - ', my_family_height[1][1], ' см')
print('Общий рост моей семьи - ',my_family_height[1][1] + my_family_height[0][1] + my_family_height[2][1] + my_family_height[3][1] + my_family_height[4][1] + my_family_height[5][1] + my_family_height[6][1], ' см')
