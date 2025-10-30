import numpy as np
import matplotlib.pyplot as plt

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

if __name__ == "__main__":
    # 1. Configuração para a derivada analítica (alta resolução)
    # Usamos um passo 'hh' muito pequeno para um gráfico suave
    hh = 0.001
    x_analitico = np.arange(-2, 2, hh)
    y_analitico = df(x_analitico)

    # 2. Configuração para as aproximações numpericas
    # Usamos um passo 'h' maior para calcular a aproximação
    h = 0.1 # Aumentar o 'h' para 0.1 para ver melhor a diferença da aproximação
    x_numerico = np.arange(-2, 2, h)

    # Calcula as aproximações nos pontos de x_numerico
    y_progressivo = aprox_progressiva(f, x_numerico, h)
    y_central = aprox_central(f, x_numerico, h)

    # 3. Exibe o gráfico
    plt.figure(figsize=(10, 6))

    # Curva analítica (suave)
    plt.plot(x_analitico, y_analitico, 'k-', label='Derivada Analítica (Exata)', linewidth=2)
    
    # Aproximações (marcadores)
    plt.plot(x_numerico, y_progressivo, 'o--', label=f'Aprox. Progressiva (h={h})')
    plt.plot(x_numerico, y_central, 's:', label=f'Aprox. Central (h={h})')

    plt.title('Comparação de Derivada Analítica vs. Numérica')
    plt.xlabel('x')
    plt.ylabel("f'(x)")
    plt.legend() # Mostra a legenda
    plt.grid(True) # Adiciona uma grade
    plt.axhline(0, color='black', linewidth=0.5) # Linha do eixo X
    plt.axvline(0, color='black', linewidth=0.5) # Linha do eixo Y

    # Mostra a figura
    plt.show()