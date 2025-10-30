import math

def metodo_bissecao(f, a, b, epsilon, max_iter):
    """
    Implementa o Algoritmo do Método da Bisseção.

    Argumentos:
    f -- A função para a qual queremos encontrar a raiz (deve ser contínua).
    a -- O início do intervalo [a, b].
    b -- O fim do intervalo [a, b].
    epsilon -- A precisão (critério de parada).
    max_iter -- O número máximo de iterações (critério de parada).
    
    Retorna:
    A raiz aproximada (x_k), ou None se o método falhar.
    """
    
    # --- Verificação da Entrada (Pré-requisito do método) ---
    # f(a) e f(b) devem ter sinais opostos
    fa = f(a)
    fb = f(b)
    
    if fa * fb >= 0:
        print(f"Erro: f(a) e f(b) não têm sinais opostos. f({a})={fa}, f({b})={fb}")
        print("O Teorema de Bolzano não pode garantir uma raiz no intervalo.")
        return None

    # --- Início ---
    k = 0 # k <- 0
    x_k = (a + b) / 2.0
    
    while (b - a) / 2.0 > epsilon and k < max_iter:
        x_k = (a + b) / 2.0 # x_k <- (a + b) / 2
        fxk = f(x_k)

        # Se encontrarmos a raiz exata (raro com floats)
        if fxk == 0:
            return x_k

        if fa * fxk < 0:
            b = x_k # Linha 6: b <- x_k
        else:
            a = x_k # a <- x_k
            fa = fxk
        
        k = k + 1 # k <- k + 1

    return x_k

if __name__ == "__main__":

    # Vamos definir a função f(x) que queremos encontrar a raiz
    # Exemplo: f(x) = x^3 - x - 2
    # f(1) = 1 - 1 - 2 = -2 (negativo)
    # f(2) = 8 - 2 - 2 = 4  (positivo)
    # A raiz está entre 1 e 2.
    
    def minha_funcao(x):
        return x**3 - x - 2

    # --- Definição da "Entrada" ---
    intervalo_a = 1.0
    intervalo_b = 2.0
    precisao = 1e-7  # (0.0000001)
    max_iteracoes = 100
    
    print(f"Método da Bisseção para f(x) = x^3 - x - 2")
    print(f"Intervalo: [{intervalo_a}, {intervalo_b}]")
    print(f"Precisão (epsilon): {precisao}")
    print(f"Máximo de iterações: {max_iteracoes}\n")

    raiz_aproximada = metodo_bissecao(minha_funcao, intervalo_a, intervalo_b, precisao, max_iteracoes)

    # Exibe o resultado
    if raiz_aproximada is not None:
        print(f"Processo concluído.")
        # O :.8f formata o número para 8 casas decimais
        print(f"A raiz aproximada é: {raiz_aproximada:.8f}")
        # O :.2e formata em notação científica (para ver se é próximo de zero)
        print(f"O valor de f(raiz) é: {minha_funcao(raiz_aproximada):.2e}")
    else:
        print("O método falhou em convergir.")