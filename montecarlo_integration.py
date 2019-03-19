import random
import matplotlib.pyplot as plt
import math


def montecarlo(f, a, b, n):
    """Вычисление интергала методом Монте Карло."""
    sum = 0
    for i in range(0, n):
        x = random.randint(a, b)
        sum += (b - a) * f(x)
    return sum / n


def f(x):
    """Функция x^3"""
    return x**3


if __name__ == '__main__':
    values = [montecarlo(f, 0, 3, 500) for n in range(1000)]
    plt.hist(values, density=True, bins=100)
    plt.show()
