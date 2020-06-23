from random import choice

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
matriz2 = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

print('-=' * 10, 'MATRIZ ORIGINAL', '-=' * 10)

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = choice(range(1, 21))
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 9, 'MATRIZ TRANSFORMADA', '-=' * 9)

for l in range(0, 4):
    for c in range(0, 4):
        if l < c:
            matriz2[l][c] = 0
        else:
            matriz2[l][c] = matriz[l][c]
        print(f'[{matriz2[l][c]:^5}]', end='')
    print()
