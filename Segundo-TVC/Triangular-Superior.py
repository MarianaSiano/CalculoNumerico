import numpy as np

def substituicao_progressiva(L, b):
    """
    Resolve o sistema linear Lx = b por substituição progressiva.
    
    Argumentos:
    L (np.array): Matriz triangular inferior (n x n).
    b (np.array): Vetor de termos independentes (n).
    
    Retorna:
    np.array: Vetor solução x (n).
    """
    
    # Obtém a dimensão 'n' do sistema
    n = L.shape[0]
    
    # Inicializa o vetor solução x com zeros
    x = np.zeros(n)

    x[0] = b[0] / L[0, 0]

    for i in range(1, n):
        s = b[i]
        for j in range(i):
            s = s - L[i, j] * x[j]
        x[i] = s / L[i, i]
    return x

# --- Exemplo de Uso ---

L = np.array([
    [2.0, 0.0, 0.0],
    [1.0, 3.0, 0.0],
    [4.0, 2.0, 1.0]
])

b = np.array([4.0, 5.0, 7.0])
x = substituicao_progressiva(L, b)

print("Matriz L:")
print(L)
print("\nVetor b:")
print(b)
print("\nSolução x:")
print(x)

# Verificação (L.x deve ser igual a b)
print("\nVerificação (L.dot(x)):")
print(L.dot(x))