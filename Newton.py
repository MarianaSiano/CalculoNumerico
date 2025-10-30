def metodo_newton(f, df, x0, epsilon, max_iter):
    """
    Implementa o Algoritmo para o Método de Newton.

    Argumentos:
    f -- A função f(x).
    df -- A derivada da função, f'(x).
    x0 -- O valor inicial.
    epsilon -- A precisão (critério de parada).
    max_iter -- O número máximo de iterações.
    
    Retorna:
    A raiz aproximada (x_k), ou None se a derivada for zero.
    """
    
    k = 1
    while k <= max_iter:
        fx0 = f(x0)
        dfx0 = df(x0)
        if dfx0 == 0:
            print("Erro: Derivada igual a zero.")
            return None
            
        x_k = x0 - (fx0 / dfx0)
        
        # Critério de parada
        if abs(x_k - x0) < epsilon or abs(f(x_k)) < epsilon:
            return x_k
        
        x0 = x_k
        k = k + 1

    print(f"Método atingiu o máximo de {max_iter} iterações sem convergir.")
    return x_k # Retorna a última aproximação

if __name__ == "__main__":    
    def funcao(x):
        return x**3 - x - 2
    
    # Derivada: f'(x) = 3x^2 - 1
    def funcao_derivada(x):
        return 3 * (x**2) - 1

    # --- Definição da "Entrada" ---
    valor_inicial_x0 = 1.5 # Chute inicial (próximo da raiz ~1.52)
    precisao = 1e-7
    max_iteracoes = 50
    
    print(f"Método de Newton para f(x) = x^3 - x - 2")
    print(f"Aproximação inicial (x0): {valor_inicial_x0}")
    print(f"Precisão (epsilon): {precisao}")
    print(f"Máximo de iterações: {max_iteracoes}\n")

    # Chama o algoritmo
    raiz_aproximada = metodo_newton(funcao, funcao_derivada, valor_inicial_x0, precisao, max_iteracoes)

    # Exibe o resultado
    if raiz_aproximada is not None:
        print(f"Processo concluído.")
        print(f"A raiz aproximada é: {raiz_aproximada:.8f}")
        print(f"O valor de f(raiz) é: {funcao(raiz_aproximada):.2e}")