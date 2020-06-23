from random import choice

matriz = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

for l in range(0, 7):
    for c in range(0, 6):
        matriz[l][c] = choice(range(50))
        print(f'[{matriz[l][c]:^3}]', end='')
    print()


def soma_coluna_matriz(matriz, coluna):
    """
    Esta função recebe uma matriz 7x6 e uma coluna e retorna a soma desta coluna.
    """
    soma = 0
    if len(matriz) == 7:
        for l in range(0, 7):
            for c in range(0, 6):
                if c == coluna:
                    soma += matriz[l][c]
        return soma
    else:
        return 'Matriz infomada não é 7x6'


coluna = int(input('Digite a coluna que deseja somar na matriz: '))
print(soma_coluna_matriz(matriz, coluna))
