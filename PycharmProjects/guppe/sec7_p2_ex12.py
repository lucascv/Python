from random import choice

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
matriz_transposta = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = choice(range(0, 51))
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 30)

for l in range(0, 3):
    for c in range(0, 3):
        matriz_transposta[l][c] = matriz[c][l]
        print(f'[{matriz_transposta[l][c]:^5}]', end='')
    print()
