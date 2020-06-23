from random import choice

matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 5):
    for c in range(0, 4):
        if c == 0:
            matriz[l][c] = choice(range(11, 21))
        elif c == 1:
            matriz[l][c] = choice(range(11))
        elif c == 2:
            matriz[l][c] = choice(range(11))
        else:
            matriz[l][c] = matriz[l][1] + matriz[l][2]

for l in range(0, 5):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^2}]', end='')
    print()

# Resolvendo letra (C) e (D)
maior_nota = 0
matricula = 0
media = 0


for l in range(0, 5):
    for c in range(0, 4):
        if c == 3:
            media += matriz[l][c]
            if matriz[l][c] > maior_nota:
                maior_nota = matriz[l][c]
                matricula = matriz[l][0]

media = media/5

print(f'A maior nota da sala foi {maior_nota} do aluno com matricula {matricula}.')
print(f'A média da notas finais da turma é {media}')
