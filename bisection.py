"""Задача найти элемент в массиве >= заданному"""
import random
import math

if __name__ == '__main__':
    # Массив для поиска элемента.
    array = range(0, 50)
    array = sorted(array)
    x = 0
    a = 0
    b = len(array) - 1
    m = (b + a) // 2
    print(x)
    print(array)

    while b - a > 1:

        if x == array[m]:
            a = m - 1
            b = m
            break

        m = (b + a) // 2

        if x < array[m]:
            b = m
        else:
            a = m

    print('Ответ: ' + str(a) + ' > x > ' + str(b))
