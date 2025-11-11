def metodo_secante(f, x0, x1, epsilon, max_iter):
    """
    Implementa o Algoritmo para o Método da Secante.

    Argumentos:
    f -- A função f(x).
    x0, x1 -- Os valores iniciais.
    epsilon -- A precisão (critério de parada).
    max_iter -- O número máximo de iterações.
    
    Retorna:
    A raiz aproximada (x_k), ou None se a divisão por zero ocorrer.
    """
    
    # O loop 'for' lida com as iterações k=2 até max_iter
    for k in range(2, max_iter + 2):
        fx0 = f(x0)
        fx1 = f(x1)
        denominador = (x1 - x0)
        
        if denominador == 0:
            print("Erro: Divisão por zero (x1 - x0 = 0).")
            return None
        d = (fx1 - fx0) / denominador
        
        if d == 0:
            print("Erro: Divisão por zero (d = 0).")
            return None
        x_k = x1 - (fx1 / d)
        
        # Critério de parada
        if abs(x_k - x1) < epsilon or abs(f(x_k)) < epsilon:
            return x_k
        
        # Prepara para a próxima iteração
        x0 = x1
        x1 = x_k

    print(f"Método atingiu o máximo de {max_iter} iterações sem convergir.")
    return x_k # Retorna a última aproximação

if __name__ == "__main__":
    def f_exemplo(x):
        return x**3 - x - 2

    # --- Definição da "Entrada" ---
    valor_inicial_x0 = 1.0
    valor_inicial_x1 = 2.0
    precisao = 1e-7
    max_iteracoes = 50
    
    print(f"Método da Secante para f(x) = x^3 - x - 2")
    print(f"Valores iniciais (x0, x1): ({valor_inicial_x0}, {valor_inicial_x1})")
    print(f"Precisão (epsilon): {precisao}")
    print(f"Máximo de iterações: {max_iteracoes}\n")

    raiz_aproximada = metodo_secante(f_exemplo, valor_inicial_x0, valor_inicial_x1, precisao, max_iteracoes)

    if raiz_aproximada is not None:
        print(f"Processo concluído.")
        print(f"A raiz aproximada é: {raiz_aproximada:.8f}")
        print(f"O valor de f(raiz) é: {f_exemplo(raiz_aproximada):.2e}")