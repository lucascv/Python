import os
from random import choice

velha = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Mostrando tabela inicial
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{velha[l][c]:^2}]', end='')
    print()
print('-=' * 20)

# Jogada 1 do usuário
pos = int(input('Digite qual posição deseja colocar sua peça: '))

for l in range(0, 3):
    for c in range(0, 3):
        if velha[l][c] == pos:
            velha[l][c] = 'X'

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{velha[l][c]:^2}]', end='')
    print()
print('-=' * 20)

# Jogada 1 do robô

x = choice([0, 2])
y = choice([0, 2])

if velha[1][1] != 'X':
    velha[1][1] = 'Y'
else:
    velha[x][y] = 'Y'

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{velha[l][c]:^2}]', end='')
    print()
print('-=' * 20)

# Jogada 2 do usuário
jogada = 0

while jogada < 1:
    pos = int(input('Digite a posição que deseja colocar sua peça: '))
    for l in range(0, 3):
        for c in range(0, 3):
            if velha[l][c] == pos:
                velha[l][c] = 'X'
                jogada += 1
    if jogada == 0:
        print('Esta posição já tem peça. Gentileza escolher outra posição.')

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{velha[l][c]:^2}]', end='')
    print()
print('-=' * 20)

# Jogada 2 do robô
qtd = 0

# Checando se possuem duas peças do usuário na mesma linha
for l in range(0, 3):
    for c in range(0, 3):
        if velha[l][c] == 'X':
            qtd += 1
    if qtd == 2:
        for c in range(0, 3):
            if velha[l][c] in ['X', 'Y']:
                qtd += 0
            else:
                velha[l][c] = 'Y'
                qtd = 0
        while qtd == 2:
            x = choice(range(0, 3))
            y = choice(range(0, 3))
            if velha[x][y] in ['X', 'Y']:
                qtd =+ 0
            else:
                velha[x][y] = 'Y'
                qtd = 0
    else:
        qtd = 0

# Chegando se possuem duas peças do usuário na mesma coluna
for c in range(0, 3):
    for l in range(0, 3):
        if velha[l][c] == 'X':
            qtd += 1
    if qtd == 2:
        for l in range(0, 3):
            if velha[l][c] in ['X', 'Y']:
                qtd += 0
            else:
                velha[l][c] = 'Y'
                qtd = 0
        while qtd == 2:
            x = choice(range(0, 3))
            y = choice(range(0, 3))
            if velha[x][y] in ['X', 'Y']:
                qtd =+ 0
            else:
                velha[x][y] = 'Y'
                qtd = 0
    else:
        qtd = 0

# Chegando se existem duas peças do usuário na diagonal:
for l in range(0, 3):
    for c in range(0, 3):
        if velha[l][c] == 'Y':
            qtd += 1
        else:
            qtd += 0

while qtd == 1:
    if velha[0][0] == 'X':
        if velha[1][1] == 'X':
            velha[2][2] == 'Y'
            qtd = 0
        elif velha[2][2] == 'X':
            velha [1][1] = 'Y'
            qtd = 0
        else:
            qtd += 0
    elif velha[0][2] == 'X':
        if velha[1][1] == 'X':
            velha[2][0] == 'Y'
            qtd = 0
        elif velha[2][0] == 'X':
            velha[1][1] == 'Y'
            qtd = 0
        else:
            qtd += 0

qtd = 0

for l in range(0, 3):
    for c in range(0, 3):
        if velha[l][c] == 'Y':
            qtd += 1
        else:
            qtd += 0

while qtd == 1:
    x = choice(range(0, 3))
    y = choice(range(0, 3))
    if velha[x][y] in ['X', 'Y']:
        qtd =+ 0
    else:
        velha[x][y] = 'Y'
        qtd = 0


print(qtd)








# Impressão do jogo da velha após jogada do robô
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{velha[l][c]:^2}]', end='')
    print()
print('-=' * 20)
