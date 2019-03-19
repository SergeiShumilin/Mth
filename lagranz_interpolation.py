import matplotlib.pyplot as plt
import numpy as np


def lagranz(x, y, t):
    """Интерполяция с помощью интерполяционного полинома Лагранжа."""

    sum = 0

    for i in range(0, len(y)):
        prod = 1

        for j in range(0, len(y)):
            if i != j:
                prod *= (t - x[j]) / (x[i] - x[j])

        sum += y[i] * prod

    return sum


def newton(x, y, t):
    """Интерполяция с помощью интерполяционного полинома Ньютона."""
    sum = 0
    print(len(y))
    for i in range(0, (len(y) - 1)):
        prod = 1
        for j in range(0, i + 1):
            prod *= t - x[j]

        sum += prod * dd(x, y, i + 2)
        print(sum)

    return dd(x, y, 1) + sum


def dd(x, y, k):
    """Разделенная разность."""
    sum = 0
    for i in range(0, k):
        prod = 1
        for j in range(0, k):
            if i != j:
                prod *= x[i] - x[j]
        sum += y[i] / prod

    return sum


def interpolation(x, func, ts, kvs):
    return [func(ts, kvs, x) for x in x]


if __name__ == '__main__':
    # Температура.
    ts = [0.0, 5.0, 10.0, 20.0, 30.0, 40.0, 50.0, 60.0,
          70.0, 80.0, 90.0, 100.0]
    # Кинематическая вязкость.
    kvs = [1.787, 1.519, 1.307, 1.004, 0.801, 0.658, 0.658, 0.475,
           0.413, 0.365, 0.326, 0.294]

    # Динамическая вязкость
    dvs = [1.787, 1.519, 1.307, 1.002, 0.798, 0.653, 0.547, 0.467,
           0.404, 0.355, 0.315, 0.282]

    x = np.arange(0, 100, 0.1)

    plt.subplot(2, 1, 1)
    plt.ylabel("Динамическая вязкость")
    plt.plot(x, interpolation(x, newton, ts, dvs), label="Интерполяция полиномом")
    plt.plot(ts, dvs, label="Табличные значения")
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.ylabel("Кинематическая вязкость")
    plt.plot(x, interpolation(x, newton, ts, kvs), label="Интерполяция полиномом")
    plt.plot(ts, kvs, label="Табличные значения")
    plt.xlabel("Температура")
    plt.legend()

    plt.show()
