from random import choice

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = choice(range(0, 51))

maior = 0
linha = 0
coluna = 0

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] > maior:
            maior = matriz[l][c]
            linha = l
            coluna = c
    print()
print('-=' * 50)

print(f'O maior elemento da matriz acima é {maior}. Sua posição é linha {linha} e coluna {coluna}.')
