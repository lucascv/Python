from random import choice

matriz = [[0, 0], [0, 0]]
matriz1 = [[0, 0], [0, 0]]

for l in range(0, 2):
    for c in range(0, 2):
        matriz[l][c] = choice(range(0, 51))
        matriz1[l][c] = choice(range(0, 51))

for l in range(0, 2):
    for c in range(0, 2):
        print(f'[{matriz[l][c]:^3}]', end='')
    print()

print('-=' * 6)

for l in range(0, 2):
    for c in range(0, 2):
        print(f'[{matriz1[l][c]:^3}]', end='')
    print()

menu = None
constante = 0
opcoes = True

print('-=' * 5, 'Digite uma das opções', '-=' * 5)
print('[A] Somar as duas matrizes acima;')
print('[B] Subtrair a primeira matriz da segunda;')
print('[C] Adicionar uma constante em ambas.')

while opcoes is True:
    menu = str(input('[A], [B] ou [C]? '))
    menu = menu.upper()
    if menu == 'A':
        opcoes = False
    elif menu == 'B':
        opcoes = False
    elif menu == 'C':
        opcoes = False
    else:
        opcoes = True

print('-=' * 21)

matriz3 = [[0, 0], [0, 0]]

if menu == 'A':
    for l in range(0, 2):
        for c in range(0, 2):
            matriz3[l][c] = matriz[l][c] + matriz1[l][c]
            print(f'[{matriz3[l][c]:^3}]', end='')
        print()

elif menu == 'B':
    for l in range(0, 2):
        for c in range(0, 2):
            matriz3[l][c] = matriz[l][c] - matriz1[l][c]
            print(f'[{matriz3[l][c]:^3}]', end='')
        print()

else:
    constante = int(input('Digite o valor da constante: '))
    for l in range(0, 2):
        for c in range(0, 2):
            matriz[l][c] = matriz[l][c] + constante
            print(f'[{matriz[l][c]:^3}]', end='')
        print()
    print('-=' * 21)
    for l in range(0, 2):
        for c in range(0, 2):
            matriz1[l][c] = matriz1[l][c] + constante
            print(f'[{matriz1[l][c]:^3}]', end='')
        print()
