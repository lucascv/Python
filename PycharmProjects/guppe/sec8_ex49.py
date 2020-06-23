from random import choice

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = choice(range(50))
        print(f'[{matriz[l][c]:^3}]', end='')
    print()


def soma_abaixo_diagonal(matriz):
    """
    Esta função recebe uma matriz 3x3 e calcula a soma dos elementos abaixo da diagonal principal
    """
    if len(matriz) == 3:
        soma = 0
        for l in range(0, 3):
            for c in range(0, 3):
                if l > c:
                    soma += matriz[l][c]
        return soma
    else:
        return 'Matriz informada não é 3x3'


print(soma_abaixo_diagonal(matriz))
