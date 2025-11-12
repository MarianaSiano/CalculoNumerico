import numpy as np

def metodo_gauss_seidel(A, b, x0, tol, max_iter):
    """
    Resolve o sistema linear Ax = b usando o Método de Gauss-Seidel.

    Argumentos:
    A (np.array): Matriz de coeficientes (n x n).
    b (np.array): Vetor de termos independentes (n).
    x0 (np.array): Suposição inicial para x (n).
    tol (float): Tolerância (critério de parada).
    max_iter (int): Número máximo de iterações.

    Retorna:
    np.array: Vetor solução x (ou a melhor aproximação).
    int: Número de iterações realizadas.
    """

    n = A.shape[0]
    x = x0.copy()

    # Loop das iterações
    for k in range(max_iter):
        
        # Armazena o 'x' da iteração anterior para verificar a convergência
        x_k_anterior = x.copy()

        # --- Implementação da fórmula da imagem ---
        # Loop 'i' (o loop 'para i = 1:n' da imagem)
        for i in range(n):
            soma = 0

            # - Se j < i, usamos x[j], que já foi ATUALIZADO (é o x^(k+1))
            # - Se j > i, usamos x[j], que ainda NÃO foi atualizado (é o x^(k))
            for j in range(n):
                if i != j:
                    soma = soma + A[i, j] * x[j]
            x[i] = (b[i] - soma) / A[i, i]
            
        # --- Critério de Parada ---
        # Verifica se a solução mudou 'pouco' da última iteração completa
        erro = np.linalg.norm(x - x_k_anterior, ord=np.inf)

        if erro < tol:
            # Convergiu!
            return x, k + 1

    # Se o loop terminar sem convergir
    print(f"Aviso: O método de Gauss-Seidel não convergiu após {max_iter} iterações.")
    return x, max_iter

# --- Exemplo de Uso ---

A = np.array([
    [10.0, 2.0, 1.0],
    [1.0, 5.0, 1.0],
    [2.0, 3.0, 10.0]
])

b = np.array([7.0, -8.0, 6.0])

# 1. Suposição inicial
x_inicial = np.zeros(3)

# 2. Tolerância
tolerancia = 1e-6

# 3. Número máximo de iterações
iteracoes_max = 100

# Executando o método
solucao, num_iter = metodo_gauss_seidel(A, b, x_inicial, tolerancia, iteracoes_max)

print(f"Matriz A:\n{A}")
print(f"\nVetor b:\n{b}")
print("\n--- Resultado (Gauss-Seidel) ---")
print(f"Solução x encontrada:\n{solucao}")
print(f"Convergência alcançada em {num_iter} iterações.")

# Verificação: A.dot(solucao) deve ser ~ b
print("\nVerificação (A.dot(x)):")
print(A.dot(solucao))