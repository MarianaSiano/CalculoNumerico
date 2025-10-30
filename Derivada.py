from pylab import *

def f(x):
    return exp(x) * sin(x)

def df(x):
    return exp(x) * sin(x) + exp(x) * cos(x)

def aprox(f, x, h):
    return (f(x + h) - f(x)) / h

def aproxCentral(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h)