from random import choice

matriz1 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz3 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print('-=' * 13, 'MATRIZ 1', '-=' * 13)

for l in range(0, 4):
    for c in range(0, 4):
        matriz1[l][c] = choice(range(0, 51))

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz1[l][c]:^5}]', end='')
    print()

print('-=' * 13, 'MATRIZ 2', '-=' * 13)

for l in range(0, 4):
    for c in range(0, 4):
        matriz2[l][c] = choice(range(0, 51))

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz2[l][c]:^5}]', end='')
    print()

print('-=' * 13, 'MATRIZ 3', '-=' * 13)

for l in range(0, 4):
    for c in range(0, 4):
        if matriz1[l][c] > matriz2[l][c]:
            matriz3[l][c] = matriz1[l][c]
        else:
            matriz3[l][c] = matriz2[l][c]

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz3[l][c]:^5}]', end='')
    print()
