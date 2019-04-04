"""Модуль строящий график производной заданной функции."""

import numpy as np
import matplotlib.pyplot as plt
import math

def f(x):
    """Экспериментальная функция x^3"""
    return math.log1p(x)


def dydx(x0, x1, y0, y1):
    """Расчитать производную на отрезке."""
    return (y1 - y0) / (x1 - x0)


def build_der_func(x, x0, dydx, y):
    """Вычислить значение функции производной на основе ур-ия прямой на каждом шаге."""
    return (x - x0) * dydx + y


def cycle(xs, der_xs, f):
    """Расчет координат графика производной."""
    y0 = 0
    res = []
    for i in range(1, len(der_xs)):
        y = f(xs[i], xs[i - 1], der_xs[i - 1], y0)
        y0 = y
        res.append(y)

    return res



if __name__ == '__main__':
    xs = np.arange(0.00001, 10, 0.00001)
    print('xs: ' + str(xs))
    der_xs = [dydx(xs[i-1], xs[i], f(xs[i-1]), f(xs[i])) for i in range(1, len(xs))]
    print(der_xs)
    #prozv = cycle(xs, der_xs, build_der_func)


    ys = [f(x) for x in xs]
    plt.plot(xs, ys, xs[:len(xs)-1], der_xs)
    plt.show()
