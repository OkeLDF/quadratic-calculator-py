#!/home/okeldf/miniconda3/bin/python

import fire
from math import sqrt
import matplotlib.pyplot as plt
import numpy as np

def calculate(a: float, b: float, c: float):
    '''calculate solution of quadratic equation ax² + bx + c = 0'''

    try:
        a = float(a)
        b = float(b)
        c = float(c)

    except Exception as e:
        print(e)

    if a == b == c == 0:
        print('invalid coefficients values: a == b == c == 0')
        return

    if a == b == 0 and c != 0:
        print(f'absurd: {c} == 0')
        return

    if a == 0:
        x = -c/b
        print(f'x = {x}')
        return

    delta = b*b - (4*a*c)

    if delta < 0:
        re = -b / (2 * a)
        im = (sqrt(-delta)) / (2 * a)
        print(f'x1 = {re} + {im} * i')
        print(f'x2 = {re} - {im} * i')
        return
    
    x1 = (-b + sqrt(delta)) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')


def plot(a: float, b: float, c: float, xlim: float = 100):
    '''plot the graph for f(x) = ax² + bx + c'''

    f = lambda x: a*x*x + b*x + c

    if a != 0:
        point = -b/(2*a)
    else:
        point = -c/b

    x_arange = np.arange(point - xlim, point + xlim + 1, 1)
    y_arange = f(x_arange)
    plt.axhline(y=0, color='gray')
    plt.axvline(x=0, color='gray')
    plt.plot(x_arange, y_arange)
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    fire.Fire({
        'calc': calculate,
        'plot': plot
    })