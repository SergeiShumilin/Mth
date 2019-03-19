"""Графики логарифмической функции и график ее производной"""

import math
import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    x = np.arange(1, 100, 0.01)
    y = [math.log2(x) for x in x]
    dy = [math.log2(math.e) / x for x in x]
    plt.plot(x, y, x, dy)
    plt.show()
