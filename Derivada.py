from pylab import *

def f(x):
    return exp(x) * sin(x)

def df(x):
    return exp(x) * sin(x) + exp(x) * cos(x)

def aprox(f, x, h):
    return (f(x + h) - f(x)) / h

def aproxCentral(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

if __name__ == "__main__":
    hh = 0.001
    xx = arange(-2, 2, hh)
    yy = df(xx)

    # Diferença progressiva e central
    h = 0.01
    x = arange(-2, 2, h)
    d1 = aprox(f, x, h)
    d2 = aproxCentral(f, x, h)

    # Exibe grafico
    # plt.figure(figsize=(8, 15))
    plot(xx, yy, label='Derivada Analítica')
    plot(x, d1, 'o-', label='Aprox. Diferença Progressiva')
    plot(x, d2, 's-', label='Aprox. Diferença Central')

    show()