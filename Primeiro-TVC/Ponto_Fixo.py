import math

def metodo_ponto_fixo(phi, x0, epsilon, max_iter):
    """
    Implementa o Algoritmo do Método do Ponto Fixo.

    Argumentos:
    phi -- A função de iteração phi(x) tal que x = phi(x).
    x0 -- A aproximação inicial.
    epsilon -- A precisão (critério de parada).
    max_iter -- O número máximo de iterações.
    
    Retorna:
    A raiz aproximada (ponto fixo x_k), ou None se o método não convergir.
    """
    
    k = 1
    while k <= max_iter:
        x_k = phi(x0)
        if abs(x_k - x0) < epsilon:
            return x_k  # Convergência alcançada
        
        x0 = x_k
        k = k + 1

    print(f"Método atingiu o máximo de {max_iter} iterações sem convergir.")
    return x_k # Retorna a última aproximação

if __name__ == "__main__":
    
    def phi(x):
        # (x + 2)^(1/3)
        # Devemos tratar raízes de números negativos se x < -2
        if x + 2 < 0:
            return -math.pow(abs(x + 2), 1/3)
        return math.pow(x + 2, 1/3)

    # --- Definição da "Entrada" ---
    aproximacao_inicial_x0 = 1.5 # Chute inicial (próximo da raiz que é ~1.52)
    precisao = 1e-7
    max_iteracoes = 100
    
    print(f"Método do Ponto Fixo para x = (x + 2)^(1/3)")
    print(f"Aproximação inicial (x0): {aproximacao_inicial_x0}")
    print(f"Precisão (epsilon): {precisao}")
    print(f"Máximo de iterações: {max_iteracoes}\n")

    # Chama o algoritmo
    raiz_aproximada = metodo_ponto_fixo(phi, aproximacao_inicial_x0, precisao, max_iteracoes)

    if raiz_aproximada is not None:
        print(f"Processo concluído.")
        print(f"A raiz aproximada (ponto fixo) é: {raiz_aproximada:.8f}")
        
        # Verificando na função original f(x) = x^3 - x - 2
        f_original = raiz_aproximada**3 - raiz_aproximada - 2
        print(f"O valor de f(raiz) é: {f_original:.2e}")