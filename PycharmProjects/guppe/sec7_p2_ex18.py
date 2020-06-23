from random import choice

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = choice(range(-21, 21))
        print(f'[{matriz[l][c]:^3}]', end='')
    print()

vetor = []
soma = 0

for c in range(0, 3):
    for l in range(0, 3):
        soma = soma + matriz[l][c]
    vetor.append(soma)
    soma = 0
print('-=' * 30)

print(vetor)
