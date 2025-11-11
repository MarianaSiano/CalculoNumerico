import numpy as np

def substituicao_retroativa(U, b):
    """
    Resolve o sistema linear Ux = b por substituição retroativa (reversa).
    (Função da sua solicitação anterior, necessária para a Eliminação Gaussiana)
    """
    n = U.shape[0]
    x = np.zeros(n)

    x[n - 1] = b[n - 1] / U[n - 1, n - 1]

    # Loop reverso de i = n - 2 até 0
    for i in range(n - 2, -1, -1):
        s = b[i]
        for j in range(i + 1, n):
            s = s - U[i, j] * x[j]
        x[i] = s / U[i, i]
    return x