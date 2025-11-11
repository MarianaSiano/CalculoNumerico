import numpy as np

def substituicao_retroativa(U, b):
    """
    Resolve o sistema linear Ux = b por substituição retroativa (reversa).
    (Função da sua solicitação anterior, necessária para a Eliminação Gaussiana)
    """
    n = U.shape[0]
    x = np.zeros(n)

    x[n - 1] = b[n - 1] / U[n - 1, n - 1]

    for i in range(n-2, -1, -1):
        s = b[i]
        for j in range(i + 1, n):
            s = s - U[i, j] * x[j]
        x[i] = s / U[i, i]
    return x

def eliminacao_gaussiana(A, b):
    """
    Resolve o sistema linear Ax = b usando Eliminação Gaussiana
    e substituição retroativa.
    
    Argumentos:
    A (np.array): Matriz de coeficientes (n x n).
    b (np.array): Vetor de termos independentes (n).
    
    Retorna:
    np.array: Vetor solução x (n).
    """
    # Para evitar modificar a matriz e o vetor originais, criamos cópias.
    # O algoritmo de eliminação transforma A em uma matriz triangular superior U.
    U = A.copy()
    b_copia = b.copy()
    
    n = U.shape[0]

    for k in range(n - 1):
        for i in range(k + 1, n):
            m = U[i, k] / U[k, k]
            for j in range(k + 1, n):
                U[i, j] = U[i, j] - m * U[k, j]
            b_copia[i] = b_copia[i] - m * b_copia[k]
    x = substituicao_retroativa(U, b_copia)
    return x

# --- Exemplo de Uso ---

# Sistema Ax = b
A = np.array([
    [2.0, 1.0, -1.0],
    [-3.0, -1.0, 2.0],
    [-2.0, 1.0, 2.0]
])

b = np.array([8.0, -11.0, -3.0])

# Solução esperada: x = [2, 3, -1]

# Resolvendo o sistema
x = eliminacao_gaussiana(A, b)

print("Matriz A original:")
print(A)
print("\nVetor b original:")
print(b)
print("\nSolução x encontrada:")
print(x)

# Verificação (A.dot(x) deve ser igual a b)
print("\nVerificação (A.dot(x)):")
print(A.dot(x))