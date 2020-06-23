matriz = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for l in range(0, 4):
    for c in range(0, 4):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 30)

for l in range(0, 4):
    for c in range(0, 4):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

maiores_10 = 0

for l in range(0, 4):
    for c in range(0, 4):
        if matriz[l][c] > 10:
            maiores_10 = maiores_10 + 1
            print(f'{matriz[l][c]} é um dos valores maiores que 10 nesta matriz.')

print(f'A matriz informada possui {maiores_10} valores maiores que 10.')
