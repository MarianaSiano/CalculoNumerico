def exp_taylor(n, x):
    fat = 1.0
    term = 1.0
    soma = term
    i = 1
    while i <= n:
        fat = fat * i
        term = term * x
        soma = soma + term / fat
        i = i + 1
    return soma

if __name__ == "__main__":
    n = int(input("Digite n => "))
    x = float(input("Digite x => ")) # Permitir valores flutuantes para x

    print(exp_taylor(n, x))