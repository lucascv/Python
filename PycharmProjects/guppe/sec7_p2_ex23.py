from random import choice

A = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
B = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        A[l][c] = choice(range(11))
        print(f'[{A[l][c]:^5}]', end='')
    print()

print('-=' * 20)

for l in range(0, 3):
    for c in range(0, 3):
        B[l][c] = A[l][c] ** 2
        print(f'[{B[l][c]:^5}]', end='')
    print()
