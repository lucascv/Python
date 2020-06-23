from random import choice

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = choice(range(50))
        print(f'[{matriz[l][c]:^3}]', end='')
    print()


def maiores_matriz(matriz):
    """
    Esta função recebe uma matriz 4x4 e retorna quantos valores maiores que 10 ela possui.
    """
    if len(matriz) == 4:
        maiores = 0
        for l in range(0, 4):
            for c in range(0, 4):
                if matriz[l][c] > 10:
                    maiores += 1
        return maiores
    else:
        'Matriz informada não é 4x4'


print(maiores_matriz(matriz))
