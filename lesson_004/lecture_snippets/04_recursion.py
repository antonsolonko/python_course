# -*- coding: utf-8 -*-

# Рекурсия - это вызов функцией самой себя

# Рассмотрим на примере факториала
# факториал N - произведение всех целых от 1 до N

# например факториал 9
# 9! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9
# 9! = 9 * 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1
# 9! = 9 * (8 * 7 * 6 * 5 * 4 * 3 * 2 * 1)
# 9! = 9 * 8!
# 9! = 9 * factorial(8) # То есть, факториал 9-ти - это 9 умноженное на функцию факториала 8-ми

# факториал 2
# 2! = 2 * factorial(1)
# 1! == 1

# в общем случае
# N * factorial(N-1)


def factorial(n):
    if n == 1:
        return 1
    factorial_n_minus_1 = factorial(n=n - 1) # Эта рекурсия вызывает саму себя, декрементация n до 1, глубина вложености равна n,
    return n * factorial_n_minus_1 # Дошли до n = 1 и функции начали схлопываться и умножать n текущей глубины и предыдущей, факториал 1! = 1 * 1


print(factorial(9))
# Смотри стек вызовов в отладчике

# рекурсия часто используется для обхода деревьев
# Document Object Module

# Получается словарь словарей словарей и так по всей вложености
html_dom = {
    'html': {
        'head': {
            'title': 'Колобок',
        },
        'body': {
            'h2': 'Привет!',
            'div': 'Хочешь, я расскажу тебе сказку?',
            'p': 'Жили-были старик со старухой...',
        }
    }
}

# Функция "ищем элемент в дереве", на вход передается некое абстрактное дерево и ищется element_name который мы ищем
def find_element(tree, element_name):
    if element_name in tree:           # Проверяем, если на нашем уровне в нашем словаре содержится этот element_name
        return tree[element_name]      # Если да то return возвращаем этот tree[element_name] из этого словаря
    for key, sub_tree in tree.items(): # Но если такого ключа нет то мы говорим for для нашего ключа и поддерева в нашем дереве делай for много раз
        if isinstance(sub_tree, dict): # Стоит проверка что элемент который мы взяли из текущего дерева - сам является словарем, что мы можем по нему бежать
            result = find_element(tree=sub_tree, element_name=element_name) # И вызываем этой нашей функции саму себя, это и есть наша рекурсия
            if result:                                                      # Но в параметрах показываем, что дерево кусок которое мы будем исследовать это sub_tree
                                                                            # То есть мы грубо говоря сначала ствол, потом рассмотрели все веточки - нет, у нас такого элемента нет как мы ищим
                                                                            # Тогда мы говорим, окей, веточка ты теперь будешь стволом, мы вызовем функцию как будто ты ствол
                                                                            # И указываем как дерево теперь растет от корня этой вот веточки и так дальше и так дальше
                                                                            # Когда функция сработает, она чтото нашла, то выход через break
                break # Конструкция поиска, если что-то нашлось то break прерывает цикл
    else:
        result = None # Если мы обошли всё дерево и ничего не нашлось тогда result = None
    return result # выход возвращение


res = find_element(tree=html_dom, element_name='div')
print(res)
