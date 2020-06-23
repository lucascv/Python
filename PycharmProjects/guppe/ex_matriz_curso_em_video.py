"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.

No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

# Somando valores pares da matriz
soma_pares = 0

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
print(soma_pares)

# Somando valores da terceira coluna
soma_coluna = 0

for l in range(0, 3):
    for c in range(2, 3):
        soma_coluna += matriz[l][c]
print(soma_coluna)

# O maior valor da segunda linha
maior_linha = 0

for l in range(1, 2):
    for c in range(0, 3):
        if matriz[l][c] > maior_linha:
            maior_linha = matriz[l][c]
print(maior_linha)
