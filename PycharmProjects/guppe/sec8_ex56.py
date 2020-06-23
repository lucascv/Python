from random import choice


def soma_linha_matriz(matriz, linha):
    """
    Esta função recebe uma matriz 7x6 e uma linha e retorna a soma da linha informada.
    """
    soma = 0
    if len(matriz) == 7:
        for l in range(0, 7):
            for c in range(0, 6):
                if l == linha:
                    soma += matriz[l][c]
        return soma
    else:
        return 'Matriz informada não é 7x6'


matriz = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

for l in range(0, 7):
    for c in range(0, 6):
        matriz[l][c] = choice(range(50))
        print(f'[{matriz[l][c]:^3}]', end='')
    print()

linha = int(input('Digite a linha que deseja somar: '))
print(soma_linha_matriz(matriz, linha))
