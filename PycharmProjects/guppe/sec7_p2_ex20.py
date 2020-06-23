matriz = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 6):
        matriz[l][c] = float(input(f'Digite um número para a posição [{l}][{c}]: '))

for l in range(0, 3):
    for c in range(0, 6):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()

# Resolvendo (A) e (B)
soma = 0
media = []

for l in range(0, 3):
    for c in range(0, 6):
        if c == 1 or c == 3:
            media.append(matriz[l][c])
        if c % 2 == 0:
            soma += matriz[l][c]

print(f'A soma dos elementos das colunas impares é {soma}.')
print(f'A média dos elementos da 2ª e 4ª coluna é {sum(media)/len(media)}')

# Resolvendo (C) e (D)
for l in range(0, 3):
    for c in range(0, 6):
        if c == 5:
            matriz[l][c] = matriz[l][0] + matriz[l][1]

for l in range(0, 3):
    for c in range(0, 6):
        print(f'[{matriz[l][c]:^6}]', end='')
    print()
