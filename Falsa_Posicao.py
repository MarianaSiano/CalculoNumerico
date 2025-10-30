def metodo_falsa_posicao(f, a, b, epsilon, max_iter):
    """
    Implementa o Algoritmo do Método da Falsa Posição (Regula Falsi).

    Argumentos:
    f -- A função para a qual queremos encontrar a raiz (deve ser contínua).
    a -- O início do intervalo [a, b].
    b -- O fim do intervalo [a, b].
    epsilon -- A precisão (critério de parada).
    max_iter -- O número máximo de iterações (critério de parada).
    
    Retorna:
    A raiz aproximada (x_k), ou None se o método falhar na verificação inicial.
    """
    
    # --- Verificação da Entrada (Pré-requisito do método) ---
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0:
        print(f"Erro: f(a) e f(b) não têm sinais opostos. f({a})={fa}, f({b})={fb}")
        print("O método da Falsa Posição não pode garantir uma raiz no intervalo.")
        return None

    # --- Início ---
    
    x_k = a 
    for k in range(max_iter):
        x_k = (a * fb - b * fa) / (fb - fa) # x_k <- (a*f(b) - b*f(a)) / (f(b) - f(a))
        fxk = f(x_k)
        if abs(fxk) < epsilon:
            print(f"Convergência alcançada em {k+1} iterações (critério f(x_k)).")
            return x_k

        if fa * fxk < 0:
            b = x_k # b <- x_k
            fb = fxk  # Otimização: reutiliza o valor já calculado
        else:
            a = x_k # a <- x_k
            fa = fxk  # Otimização: reutiliza o valor já calculado
        
        # Linha 9 (k <- k + 1) é tratada pelo loop 'for'

    # Se o loop terminar sem 'return', o máximo de iterações foi atingido
    print(f"Método atingiu o máximo de {max_iter} iterações sem convergir.")
    return x_k

if __name__ == "__main__":    
    def funcao(x):
        return x**3 - x - 2

    intervalo_a = 1.0
    intervalo_b = 2.0
    precisao = 1e-7  # (0.0000001)
    max_iteracoes = 100
    
    print(f"Método da Falsa Posição para f(x) = x^3 - x - 2")
    print(f"Intervalo: [{intervalo_a}, {intervalo_b}]")
    print(f"Precisão (epsilon): {precisao}")
    print(f"Máximo de iterações: {max_iteracoes}\n")

    # Chama o algoritmo
    raiz_aproximada = metodo_falsa_posicao(funcao, intervalo_a, intervalo_b, precisao, max_iteracoes)

    if raiz_aproximada is not None:
        print(f"Processo concluído.")
        print(f"A raiz aproximada é: {raiz_aproximada:.8f}")
        print(f"O valor de f(raiz) é: {funcao(raiz_aproximada):.2e}")
    else:
        print("O método falhou em encontrar uma raiz.")