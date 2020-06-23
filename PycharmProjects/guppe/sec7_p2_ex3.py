from random import choice

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = choice(range(0, 51))
print('-=' * 50)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 50)

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = matriz[l][c] * matriz[l][c]

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
