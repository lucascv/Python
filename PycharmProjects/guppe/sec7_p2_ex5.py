matriz = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

for l in range(0, 5):
    for c in range(0, 5):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('-=' * 30)

for l in range(0, 5):
    for c in range(0, 5):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-=' * 30)

x = int(input('Digite o valor que deseja buscar na matriz: '))
qtd = 0

for l in range(0, 5):
    for c in range(0, 5):
        if matriz[l][c] == x:
            print(f'O valor {x} se encontra na posição [{l}, {c}].')
            qtd = qtd + 1

if qtd == 0:
    print(f'O valor {x} não foi encontrado na matriz acima.')
else:
    print(f'O valor {x} foi encontrado {qtd}x na matriz acima.')
