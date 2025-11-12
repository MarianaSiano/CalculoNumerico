import numpy as np

def decomposicao_lu_doolittle(A):
    """
    Realiza a decomposição A = LU usando o Método de Doolittle.
    Esta é a implementação correta das FÓRMULAS no topo da sua imagem,
    corrigindo os loops do PSEUDOCÓDIGO da imagem.
    
    Argumentos:
    A (np.array): Matriz de coeficientes (n x n).
    
    Retorna:
    (np.array, np.array): Tupla contendo as matrizes L e U.
    """
    
    n = A.shape[0]
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    
    # O loop 'i' do pseudocódigo é o 'k' aqui (mais comum)
    for k in range(n):
        L[k, k] = 1.0
        for j in range(k, n):
            soma_u = 0
            for p in range(k):
                soma_u += L[k, p] * U[p, j]
            U[k, j] = A[k, j] - soma_u

        for i in range(k + 1, n):
            soma_l = 0
            for p in range(k):
                soma_l += L[i, p] * U[p, k]
            if U[k, k] == 0:
                raise ValueError(f"Pivô U[{k},{k}] é zero. A decomposição LU ingênua falhou.")
            L[i, k] = (A[i, k] - soma_l) / U[k, k]
            
    return L, U

# --- Exemplo de Uso ---

# Matriz A do seu exercício (c)
A = np.array([
    [5.0, 2.0, 1.0],
    [3.0, 1.0, 4.0],
    [1.0, 1.0, 3.0]
])

print("Matriz Original A:")
print(A)

try:
    L, U = decomposicao_lu_doolittle(A)

    print("\nMatriz L (Triangular Inferior):")
    print(L)
    print("\nMatriz U (Triangular Superior):")
    print(U)
    
    # Verificação: L.dot(U) deve ser igual a A
    print("\nVerificação (L.dot(U)):")
    print(L.dot(U))
    
except ValueError as e:
    print(f"\nErro: {e}")