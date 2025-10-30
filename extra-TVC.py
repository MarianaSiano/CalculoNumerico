import math

def f_problema(x):
    """
    Define a equação do problema: f(x) = x - 5e^(-x)
    """
    return x - 5 * math.exp(-x)

def metodo_secante_exercicio(f, x0, x1, epsilon, max_iter):
    """
    Implementa o Método da Secante com o critério de parada de erro relativo
    especificado no exercício: |x_k - x_k-1| / |x_k| <= epsilon.

    Argumentos:
    f -- A função f(x)
    x0, x1 -- Valores iniciais (x_k-2 e x_k-1, respectivamente)
    epsilon -- Precisão (tolerância do erro relativo)
    max_iter -- Número máximo de iterações
    
    Retorna:
    A raiz aproximada (x_k), ou None se o método falhar.
    """
    
    print("Iniciando Método da Secante (Critério de Erro Relativo)")
    print(" k |   x_k-1      |     x_k        | f(x_k)       | Erro Relativo")
    print("-" * 65)

    # Inicializa os valores de f(x) para os dois primeiros pontos
    fx0 = f(x0)
    fx1 = f(x1)

    # O loop 'for' itera 'max_iter' vezes.
    # Usamos 'k' para contar as iterações (começando da 2ª)
    for k in range(2, max_iter + 2):
        # Denomidador da fórmula da secante
        denominador_formula = (fx1 - fx0)

        # Proteção contra divisão por zero
        if abs(denominador_formula) < 1e-15:
            print("Erro: Divisão por zero (f(x_k-1) - f(x_k-2) é muito pequeno).")
            print("O método falhou em convergir.")
            return None

        # Fórmula da Secante (calcula x_k)
        # x_k = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        x_k = x1 - fx1 * (x1 - x0) / denominador_formula
        
        # Calcula o valor da função no novo ponto
        fxk = f(x_k)

        # --- Critério de Parada ---
        # Erro = |x_k - x_k-1| / |x_k|
        erro_relativo = float('inf')
        if abs(x_k) > 1e-15: # Evita divisão por zero se a raiz for ~0
            erro_relativo = abs(x_k - x1) / abs(x_k)
        else:
            erro_relativo = abs(x_k - x1) # Fallback para erro absoluto

        # Exibe a iteração atual
        print(f"{k:<2} | {x1:12.9f} | {x_k:12.9f} | {fxk:12.3e} | {erro_relativo:12.3e}")

        # 1. Verifica o critério de parada principal (erro relativo)
        if erro_relativo <= epsilon:
            print("-" * 65)
            print(f"Convergência alcançada na iteração {k} (Erro Relativo <= {epsilon}).")
            return x_k
        
        # 2. Verifica um critério de parada secundário (f(x) perto de zero)
        if abs(fxk) <= epsilon:
            print("-" * 65)
            print(f"Convergência alcançada na iteração {k} (|f(x_k)| <= {epsilon}).")
            return x_k

        # --- Prepara para a próxima iteração ---
        # O ponto 'anterior' (x0) se torna o 'atual' (x1)
        x0 = x1
        fx0 = fx1
        
        # O ponto 'novo' (x_k) se torna o 'atual' (x1)
        x1 = x_k
        fx1 = fxk

    # Se o loop terminar, o máximo de iterações foi atingido
    print("-" * 65)
    print(f"Método atingiu o máximo de {max_iter} iterações sem convergir.")
    return x_k

if __name__ == "__main__":

    # --- Entradas do Exercício ---
    x_inicial_0 = 1.4
    x_inicial_1 = 1.5
    precisao_epsilon = 1e-8  # (10**-8)
    max_iteracoes = 50
    
    print(f"Resolvendo f(x) = x - 5*exp(-x) = 0")
    print(f"Aproximações iniciais: x0 = {x_inicial_0}, x1 = {x_inicial_1}")
    print(f"Precisão (epsilon): {precisao_epsilon}\n")

    # Chama o algoritmo
    raiz_aproximada = metodo_secante_exercicio(f_problema, x_inicial_0, x_inicial_1, precisao_epsilon, max_iteracoes)

    # Exibe o resultado final
    if raiz_aproximada is not None:
        print(f"\n--- Resultado Final ---")
        print(f"A raiz positiva encontrada é: {raiz_aproximada:.10f}")
        print(f"O valor de f(raiz) é:       {f_problema(raiz_aproximada):.2e}")