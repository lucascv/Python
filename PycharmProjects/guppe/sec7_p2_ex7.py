"""
matriz = []
m = int(input('Digite o numero de linhas da matriz: '))
n = int(input('Digite o numero de colunas da matriz: '))

def constroiMatriz(m, n, matriz):
    for i in range(1, m+1):
        linha = []
        for j in range(1, n+1):
            x = int(input(f'Digite o elemento [{i}, {j}] da matriz: '))
            linha.append(x)

        matriz.append(linha)

constroiMatriz(m, n, matriz)

print(matriz)
"""
matriz = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

for l in range(0, 10):
    for c in range(0, 10):
        if l < c:
            matriz[l][c] = (2 * l) + (7 * c) - 2
        elif l == c:
            matriz[l][c] = (3 * (l ** 2)) - 1
        else:
            matriz[l][c] = (4 * (l ** 3)) - (5 * (c ** 2)) + 1

for l in range(0, 10):
    for c in range(0, 10):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
