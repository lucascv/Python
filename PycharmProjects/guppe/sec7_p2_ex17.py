from random import choice

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
pior_nota = 11
pior_prova = None
piores = {0: 0, 1: 0, 2: 0}

for l in range(0, 10):
    for c in range(0, 3):
        matriz[l][c] = choice(range(0, 11))
        print(f'[{matriz[l][c]:^2}]', end='')
    print()

for l in range(0, 10):
    for c in range(0, 3):
        if matriz[l][c] < pior_nota:
            pior_nota = matriz[l][c]
            pior_prova = c
    piores[pior_prova] = piores[pior_prova] + 1
    pior_prova = None
    pior_nota = 11

print(f'São {piores[0]} alunos com a pior nota na primeira prova.')
print(f'São {piores[1]} alunos com a pior nota na segunda prova.')
print(f'São {piores[2]} alunos com a pior nota na terceira prova.')
