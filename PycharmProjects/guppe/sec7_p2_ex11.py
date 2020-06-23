from random import choice

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = choice(range(0, 51))
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

soma = 0
aux = 2

for l in range(0, 3):
    soma = soma + matriz[l][aux]
    aux = aux - 1
print(f'A soma dos números na diagonal secundária é {soma}.')
