n = int(input('Digite um número: '))
cont = 0

for num in range(1, n + 1):
    if n % num == 0:
        cont = cont + 1

if cont != 2:
    print('Numero NÃO é primo.')
else:
    print('Número primo.')
