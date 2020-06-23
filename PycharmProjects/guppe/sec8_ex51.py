from random import choice

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = choice(range(50))
        print(f'[{matriz[l][c]:^3}]', end='')
    print()


def soma_diagonal_secundaria(matriz):
    """
    Esta função calcula a soma da diagonal secundária de uma matriz 3x3.
    """
    if len(matriz) == 3:
        aux = 2
        soma = 0
        for l in range(0, 3):
            soma += matriz[l][aux]
            aux -= 1
        return soma
    else:
        return 'Matriz informada não é 3x3'


print(soma_diagonal_secundaria(matriz))
