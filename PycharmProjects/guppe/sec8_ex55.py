from random import choice

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = choice(range(10))
        print(f'[{matriz[l][c]:^3}]', end='')
    print()


def soma_diagonais(matriz):
    """
    Esta função recebe uma matriz 3x3 e retorna a soma dos elementos na diagonal principal e secundária.
    """
    if len(matriz) == 3:
        soma = 0
        aux = 2
        for l in range(0, 3):
            for c in range(0, 3):
                if l == c:
                    soma += matriz[l][c]
        for l in range(0, 3):
            soma += matriz[l][c]




    else:
        return 'Matriz informada não é 3x3'