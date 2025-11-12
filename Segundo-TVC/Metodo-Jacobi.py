import numpy as np

def metodo_jacobi(A, b, x0, tol, max_iter):
    """
    Resolve o sistema linear Ax = b usando o Método de Jacobi.

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

    # x_k será o vetor da iteração anterior (k)
    # x_k1 será o novo vetor da iteração atual (k+1)
    x_k = x0.copy()
    x_k1 = np.zeros(n)

    # Loop das iterações
    for k in range(max_iter):

        # Loop 'i' (o loop 'para i=1:n' da imagem)
        for i in range(n):

            # 1. b_i
            soma = b[i]

            # 2. Subtrai a Soma(a_ij * x_j^k)
            # (Usamos um loop j para somar, exceto quando j=i)
            for j in range(n):
                if i != j:
                    soma = soma - A[i, j] * x_k[j]

            # 3. Divide por a_ii
            x_k1[i] = soma / A[i, i]
            
        # --- Critério de Parada ---
        erro = np.linalg.norm(x_k1 - x_k, ord=np.inf)

        # Atualiza x_k para a próxima iteração
        x_k = x_k1.copy()

        if erro < tol:
            # Convergiu!
            return x_k, k + 1

    # Se o loop terminar sem convergir
    print(f"Aviso: O método de Jacobi não convergiu após {max_iter} iterações.")
    return x_k, max_iter

# --- Exemplo de Uso ---

A = np.array([
    [10.0, 2.0, 1.0],
    [1.0, 5.0, 1.0],
    [2.0, 3.0, 10.0]
])

b = np.array([7.0, -8.0, 6.0])

# 1. Suposição inicial (pode ser qualquer coisa, zeros é comum)
x_inicial = np.zeros(3)

# 2. Tolerância (quão preciso queremos o resultado)
tolerancia = 1e-6

# 3. Número máximo de iterações (para evitar loop infinito)
iteracoes_max = 100

# Executando o método
solucao, num_iter = metodo_jacobi(A, b, x_inicial, tolerancia, iteracoes_max)

print(f"Matriz A:\n{A}")
print(f"\nVetor b:\n{b}")
print("\n--- Resultado ---")
print(f"Solução x encontrada:\n{solucao}")
print(f"Convergência alcançada em {num_iter} iterações.")

# Verificação: A.dot(solucao) deve ser ~ b
print("\nVerificação (A.dot(x)):")
print(A.dot(solucao))