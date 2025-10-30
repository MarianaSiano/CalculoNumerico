import numpy as np
import matplotlib as plt

def f(x):
    """Função original."""
    return np.exp(x) * np.sin(x)

def df(x):
    """Derivada analítica (exata) de f(x)."""
    return np.exp(x) * (np.sin(x) + np.cos(x))

def aprox_progressiva(f, x, h):
    """Aproximação da derivada pela diferença progressiva (forward difference)."""
    return (f(x + h) - f(x)) / h

def aprox_central(f, x, h):
    """Aproximação da derivada pela diferença central (central difference)."""
    return (f(x + h) - f(x - h)) / (2 * h)