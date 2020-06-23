from random import choice

A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
C = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        A[l][c] = choice(range(51))
        print(f'[{A[l][c]:^3}]', end='')
    print()

print('-=' * 10)

for l in range(0, 3):
    for c in range(0, 3):
        B[l][c] = choice(range(51))
        print(f'[{B[l][c]:^3}]', end='')
    print()

print('-=' * 10)
# Criando matriz C

for l in range(0, 3):
    for c in range(0, 3):
        C[l][c] = A[l][c] * B[l][c]
        print(f'[{C[l][c]:^5}]', end='')
    print()

