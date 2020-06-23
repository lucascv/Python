from random import choice


def soma_matriz(matriz):
    """
    Esta função recebe uma matriz 4x4 e retorna a soma de seus elementos.
    """
    soma = 0
    for l in range(0, 4):
        for c in range(0, 4):
            soma += matriz[l][c]
    return soma


matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = choice(range(10))
        print(f'[{matriz[l][c]:^3}]', end='')
    print()


print(soma_matriz(matriz))
