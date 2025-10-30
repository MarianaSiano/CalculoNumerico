def exp_taylor(n, x):
    fat = 1.0
    term = 1.0
    sum = term
    i = 1
    while i <= n:
        fat = fat * i
        term = term * x
        sum = sum + term / fat
        i = i + 1
    return sum

if __name__ == "__main__":
    n = int(input("Digite n => "))
    x = int(input("Digite x => "))

    print (exp_taylor(n, x))