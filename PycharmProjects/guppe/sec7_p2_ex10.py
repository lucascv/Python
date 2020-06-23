from random import choice

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = choice(range(0, 51))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

soma = 0

for l in range(0, 3):
    for c in range(0, 3):
        if l == c:
            soma = soma + matriz[l][c]

print(f'A soma dos elementos na diagonal principal é {soma}.')
